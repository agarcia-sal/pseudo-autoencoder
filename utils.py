import os
import math
import importlib.util
import openai
import re
import textwrap
import signal
import sys
import io
import concurrent.futures
import ast
import contextlib
from tqdm import tqdm
import subprocess
import multiprocessing as mp
import json
import pandas
import psutil
import signal
import subprocess
import os
import signal
import multiprocessing as mp
import fcntl
import pyphen
import textstat
from pathlib import Path
from openai import OpenAI
from typing import Dict, Optional

import cloudpickle
from multiprocessing.reduction import ForkingPickler
from utils.llm_client.base import BaseClient
from evaluation.eval_dataset.execution import swallow_io, time_limit, unsafe_execute


# Use cloudpickle to support pickling dynamic functions.
ForkingPickler.dumps = cloudpickle.dumps


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException("Execution time exceeded 60 seconds")


def read_file(path):
    return "".join([line for line in open(path)])


def write_to_file(filename: str, content: str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def import_func(path, *var_names):
    # Use the filename (without extension) as the module name.
    module_name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return (getattr(module, var) for var in var_names)


def read_eval_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred while reading the file: {e}"


def list_dirs(path="."):
    return sorted([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

def list_test_cases(path="."):
    return sorted(
        f for f in os.listdir(path)
        if not (f.endswith(".py") or f == "__pycache__")
    )

def list_jsonl_task_ids(path="."):
    task_ids = []
    jsonl_files = [file for file in os.listdir(path) if file.endswith('.jsonl')]
    filename = os.path.join(path, jsonl_files[0])
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            json_obj = json.loads(line.strip())
            task_ids.append(json_obj.get("task_id")) #returns 'None' if "name" doesn't exist

    return task_ids

def list_problem_cases(path="."):
    return sorted(
        f for f in os.listdir(path)
        if not (f.endswith(".py") or f == "__pycache__" or f == "metrics")
    )


class FileLock:
    def __init__(self, lock_file_path='cpu.lock'):
        self.lock_file_path = lock_file_path
        self.lock_file = None

    def __enter__(self):
        # Open (or create) the lock file
        self.lock_file = open(self.lock_file_path, "w")
        # Acquire an exclusive lock (this will block until the lock is available)
        fcntl.flock(self.lock_file, fcntl.LOCK_EX)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Release the lock and close the file
        fcntl.flock(self.lock_file, fcntl.LOCK_UN)
        self.lock_file.close()

class CostTracker:
    total_cost_usd = 0.0

    @classmethod
    def add_cost(cls, cost: float):
        cls.total_cost_usd += cost

    @classmethod
    def get_total_cost(cls) -> float:
        return cls.total_cost_usd



def call_llm(question: str, client, model, reasoning_effort=None) -> str:
    # previously: model='openai/gpt-4o'
    # from litellm import completion
    # messages = [{"content": question, "role": "user"}]
    # response = completion(model=model, messages=messages, reasoning_effort=reasoning_effort)
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": question,
    #         }
    #     ],
    #     # model="gpt-4o-mini",
    #     model=model, #switching to 4o because hit requests per day (RPD) rate limit for 4o-mini
    # )
    message = [
        {
            "role": "user",
            "content": question,
        }
    ]
    message_list = [message]
    return client.multi_chat_completion(message_list)[0]
    # return chat_completion.choices[0].message.content
    # return response.choices[0].message.content


def extract_and_compile_code(llm_answer: str):
    # This function is still useful for testing in the main process if needed.
    code_blocks = re.findall(r"```python(.*?)```", llm_answer, re.DOTALL)
    if not code_blocks:
        raise ValueError("No Python code block found in the LLM response.")
    extracted_code = textwrap.dedent(code_blocks[0])
    if "def solve(" not in extracted_code:
        raise ValueError("Extracted code does not define a function named 'solve'.")
    namespace = {}
    try:
        exec(extracted_code, namespace)
    except Exception as e:
        raise RuntimeError(f"Error executing the extracted code: {e}")
    if "solve" not in namespace or not callable(namespace["solve"]):
        raise ValueError("Extracted code does not contain a valid 'solve' function.")
    return namespace["solve"]


def extract_function_source(file_path: str, function_name: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source, filename=file_path)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            start_line = node.lineno - 1
            if not hasattr(node, 'end_lineno'):
                raise RuntimeError("Python 3.8+ is required for this function to work properly.")
            end_line = node.end_lineno
            source_lines = source.splitlines()
            function_source = "\n".join(source_lines[start_line:end_line])
            return function_source
    raise ValueError(f"Function '{function_name}' not found in the file '{file_path}'.")


def design_optimal(problem_cases, K):
    def simulate(N, M):
        slots = [0] * N
        for cases in problem_cases.values():
            t = math.ceil(len(cases) / M)
            slots[slots.index(min(slots))] += t
        return max(slots)

    best_time, best_N, best_M = float('inf'), None, None
    P = len(problem_cases)

    for N in range(1, P + 1):
        M = K // N
        if M < 1:
            continue
        total_time = simulate(N, M)
        # Prefer smaller N if total_time is the same
        if total_time < best_time or (total_time == best_time and N < best_N):
            best_time, best_N, best_M = total_time, N, M

    return best_N, best_M

@contextlib.contextmanager
def capture_all_output():
    buffer = io.StringIO()
    # Save the original stdout and stderr
    old_stdout, old_stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = buffer, buffer
    # For subprocess calls that expect file descriptors, we may need to use the actual file descriptor
    stdout_fd = old_stdout.fileno()
    stderr_fd = old_stderr.fileno()
    saved_stdout_fd = os.dup(stdout_fd)
    saved_stderr_fd = os.dup(stderr_fd)
    try:
        yield buffer
    finally:
        # Restore original stdout and stderr
        sys.stdout, sys.stderr = old_stdout, old_stderr
        os.dup2(saved_stdout_fd, stdout_fd)
        os.dup2(saved_stderr_fd, stderr_fd)
        os.close(saved_stdout_fd)
        os.close(saved_stderr_fd)



class ParallelRun:
    def __init__(self, func, *args, **kwargs):
        self.func = func

    def evaluate_instance_in_subprocess(self, idx, code_solution_path, problem_file_path, config_path, queue):
        """
        Run evaluation inside a process and store its PID in a global variable
        so we can identify its children later if needed.
        """
        try:
            # Set process group ID to make it easier to kill all children later
            if hasattr(os, 'setpgrp'):  # Unix/Linux/Mac
                os.setpgrp()

            result = 1
            # result = run_test_case(problem_file_path, code_solution_path, idx, timestamp, iter, round, stage)
            # print(f'result in evaluate_instance_in_subprocess(): {result}', flush=True)

            # Re-import eval_func from the config file.
            # _, eval_func = import_func(config_path, 'load_data', 'eval_func')
            # # Compile the solve function from its source code.
            # local_namespace = {}
            # exec(code_solution, local_namespace)
            # if "solve" not in local_namespace:
            #     raise ValueError("The source code does not define a 'solve' function.")
            # solve_func = local_namespace["solve"]
            # # result = evaluate_instance(instance, solve_func, eval_func)

            # with capture_all_output(): # this is myabe where i want to capture the code, pseudocode, errors and what not
            #     result = self.func(instance, solve_func, eval_func)
            queue.put(result)
        except Exception as e:
            queue.put(f"Exception: {str(e)}")



    def run_instance_with_timeout(self, idx, code_solution_path, problem_file_path, config_path, timeout):
        # Create a unique cgroup name for this instance.
        # (You might use a unique identifier from the instance or the process PID)
        # cgroup_name = f"experiment_{os.getpid()}_{instance.get('id', 'unknown')}" #[TO DO]: commented this out but i might need it??

        # Create a cgroup for CPU and memory (adjust as needed for your system, and note this works for cgroup v1)
        # subprocess.run(["cgcreate", "-g", f"cpu,memory:/{cgroup_name}"],
        #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        unit_test_idx = idx + 1 # add 1 because inputs and outputs for unit tests are not 0-indexed
        queue = mp.Queue()
        p = mp.Process(target=self.evaluate_instance_in_subprocess,
                       args=(unit_test_idx, code_solution_path, problem_file_path, config_path, queue))
        p.start()

        # Add the process to the cgroup
        # subprocess.run(["cgclassify", "-g", f"cpu,memory:/{cgroup_name}", str(p.pid)],
        #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        p.join(timeout + 1)  # 1 extra second
        if p.is_alive():
            p.terminate()
            try:
                parent = psutil.Process(p.pid)
                it = 1
                for child in parent.children(recursive=True):
                    if it > 100:
                        break
                    child.kill()
                    it += 1
                parent.kill()
            except psutil.NoSuchProcess:
                pass
            p.join(1)
            # Kill all processes in the cgroup (including detached pulp solvers)
            # subprocess.run(["cgdelete", "-g", f"cpu,memory:/{cgroup_name}"],
            #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return f"Timeout ({timeout}s)"
        else:
            try:
                result = queue.get_nowait()
            except Exception:
                result = "No result"
            # subprocess.run(["cgdelete", "-g", f"cpu,memory:/{cgroup_name}"],
            #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return result
        
    def get_code_solution(self, problem_file_path, prompt, prev_stage_prompt, timeout, stage, timestamp, it, round, client):
        # client = OpenAI(
        #     # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        #     api_key = os.getenv('OPENAI_API_KEY'),
        # )

        if stage == 'encoder':
            encoding_prompt = prompt
            decoding_prompt = prev_stage_prompt
        else:
            encoding_prompt = prev_stage_prompt
            decoding_prompt = prompt
        model = 'gpt-4.1-mini'

        # starter_code_path = os.path.join(problem_file_path, "llm_scripting", "starter_code.py") # [TO DO]: create a timestamp folder for the generated code
        # starter_code = file_to_string(starter_code_path)

        description_path = os.path.join(problem_file_path,"description", "description.txt")
        description = file_to_string(description_path)

        # pseudocode_encoding = call_llm(encoding_prompt + "\nCode to translate:" +  starter_code, client, model) 
        pseudocode_encoding = call_llm(encoding_prompt + "\nProblem Description:" +  description, client, model) 
        code_decoding = call_llm(decoding_prompt +  "\nPseudocode to translate:" + pseudocode_encoding, client, model ) 
        code_blocks = extract_code_blocks(code_decoding) #[TO DO]: I think this is needed? but not sure
        code = textwrap.dedent(code_blocks[0])
        # print('pseudocode: ', pseudocode_encoding)
        # print('code: ', code)
        #write code_solution and pseudocode to a path and return the path
        code_file_path = os.path.join(problem_file_path, "outputs", "decoded_codes", timestamp, f"iter_{it}_round_{round}_generated_code.py")
        with open(code_file_path, 'w') as file:
            file.write(code)
        pseudocode_file_path = os.path.join(problem_file_path, "outputs", "pseudocodes", timestamp, f"iter_{it}_round_{round}_pseudocode_encoding.txt")
        with open(pseudocode_file_path, 'w') as file:
            file.write(pseudocode_encoding)
        return code_file_path, pseudocode_encoding


    def process_single_problem_parallel(self, problem, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timeout, timestamp, it, round, instance_workers):
        # print(f"Processing {problem}", flush=True)
        # return problem, {"metric": 1.0}, ([1.0], None)
        # print('in process_single_problem')
        file_path = os.path.join(src_dir, dataset_name, problem)
        # list_of_instance = load_data(file_path)
        # inst_total = len(list_of_instance)
        inst_total = get_num_test_cases(file_path)
        # print(f'inst_total in process_single_problem(): {inst_total}', flush=True)
        instance_results = [None] * inst_total

        code_solution_path, pseudocode_encoding = self.get_code_solution(file_path, prompt, prev_stage_prompt, timeout, stage, timestamp, it, round)
        # print(f'code_solution_path: {code_solution_path}', flush=True)
        # print(f'pseudocode_encoding: {pseudocode_encoding}', flush=True)
        metrics = get_metrics(pseudocode_encoding)
        if metrics == None:
            metrics = {}
        # print(f'metrics in process_single_problem(): {metrics}', flush=True)

        with concurrent.futures.ThreadPoolExecutor(max_workers=instance_workers) as instance_executor:
            future_to_idx = {
                instance_executor.submit(self.run_instance_with_timeout, idx, code_solution_path, file_path, config_path, timeout): idx
                for idx in range(inst_total)
            }
            for future in concurrent.futures.as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    result = future.result()
                except Exception as e:
                    result = f"Exception: {str(e)}"
                instance_results[idx] = result

        return problem, metrics, (instance_results, None) # None refers to no answer


    def process_all_problems_parallel(self, problem_cases, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, round,
                          timeout=60, instance_workers=4, case_workers=4):
        results = {}
        metrics = {}
        # print('case workers: ', case_workers)
        # print('instance_workers: ', instance_workers)
        # print('problem_cases in process_all_problems: ', problem_cases)
        pbar = tqdm(total=len(problem_cases), desc=f"Processing cases for '{dataset_name}'", unit="case")

        # Submit each case processing as an independent process.
        with concurrent.futures.ProcessPoolExecutor(max_workers=case_workers) as case_executor:
            future_to_case = {
                case_executor.submit(
                    self.process_single_problem, problem, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timeout, timestamp, it, round,
                    instance_workers
                ): problem for problem in problem_cases
            }
            # print('future_to_case: ', future_to_case)
            for future in concurrent.futures.as_completed(future_to_case):
                try:
                    # print('right before getting result() in try case:')
                    problem_case, problem_metrics, case_result = future.result()
                    # print('problem_case: ', problem_case)
                    # print('problem_metrics: ', problem_metrics)
                    # print('case_result: ', case_result)
                except Exception as e:
                    problem_case = future_to_case[future]
                    case_result = (None, f"Exception: {str(e)}")
                    problem_metrics = None # [TO DO]: in normalize_metrics() and average_metrics(), check for when metrics is none
                results[problem_case] = case_result
                metrics[problem_case] = problem_metrics
                pbar.update(1)
        pbar.close()
        print('metrics in process_all_problems(): ', metrics)
        return results, metrics
    
    def gen_multi_chat_encodings(self, dataset_name, problem_file_path_list, encoding_prompt, stage, timestamp, it, client):
        message_list = []

        #[TO DO]: I think actually problem_file_path_list should be the path to the json file. cause i don't think it makes
        # much sense to pass in the task_ids... right? i am going to have to iterate through the jsonl file anyway.
        task_ids = []
        jsonl_files = [file for file in os.listdir(dataset_name) if file.endswith('.jsonl')]
        filename = os.path.join(dataset_name, jsonl_files[0])
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                json_obj = json.loads(line.strip())
                starter_code = json_obj.get("prompt") + json_obj.get("canonical_solution")
                task_id = json_obj.get("task_id")
                task_ids.append(task_id)


        # for problem_file_path in problem_file_path_list:
        #     starter_code_path = os.path.join(problem_file_path, "llm_scripting", "starter_code.py")
        #     starter_code = file_to_string(starter_code_path)

                encoding_prompt_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "prompts", f"{task_id}_{stage}_stage_encoding_prompt.txt")
                with open(encoding_prompt_file_path, 'w') as file: 
                    file.write(encoding_prompt)

                # minified_code = minify(starter_code, rename_locals=True, remove_annotations=True, remove_literal_statements=True)
                # description_path = os.path.join(problem_file_path,"description", "description.txt")
                # description = file_to_string(description_path)

                message=[
                    {
                        "role": "user",
                        # "content": encoding_prompt + "\nProblem Description:" +  description,
                        "content": encoding_prompt + "\nCode to translate:" +  starter_code,
                    }
                ]
                message_list.append(message)
            pseudocode_encoding_list = client.multi_chat_completion(message_list)
        

        # Write pseudocodes to file
        # for idx, problem_file_path in enumerate(problem_file_path_list):
        for idx, task_id in enumerate(task_ids):
            pseudocode = pseudocode_encoding_list[idx]
            # pseudocode_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "pseudocodes", f"pseudocode_{stage}.txt")
            pseudocode_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "pseudocodes", f"{task_id}_pseudocode_{stage}.txt")
            with open(pseudocode_file_path, 'w') as file:
                file.write(pseudocode)
    
        return pseudocode_encoding_list
    
    def gen_multi_chat_decodings(self, dataset_name, problem_cases, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, client):
        message_list = []
        for pseudocode in pseudocode_encoding_list:
            message=[
                {
                    "role": "user",
                    "content": decoding_prompt + "\nPseudocode to translate:" +  pseudocode,
                }
            ]
            message_list.append(message)
        code_decodings = client.multi_chat_completion(message_list)
        # print('code decodings:', code_decodings)
        # print('length of code_decodings: ', len(code_decodings))
        # print('length of pseudocode encodings: ', len(pseudocode_encoding_list))

        # Write codes to file:
        code_file_path_list = []
        task_decoded_codes = {}
        # for idx, problem_file_path in enumerate(problem_file_path_list):
        for idx, problem in enumerate(problem_cases):
            decoding = code_decodings[idx]
            code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
            if len(code_blocks) == 0:
                code_blocks = decoding # in case the prompt didn't output ```python``` formatting, is this the best way to do this?
            # print('code blocks in gen_multi_chat_decodings(): ', code_blocks)
            code = textwrap.dedent(code_blocks[0])
            # code = textwrap.dedent(decoding)

            # code_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "decoded_codes", f"generated_code_{stage}.py")
            code_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "decoded_codes", f"{problem}_decoded_code_{stage}.py")
            with open(code_file_path, 'w') as file:
                file.write(code)
            # code_file_path_list.append(code_file_path)
            task_decoded_codes[problem] = task_decoded_codes

            # decoding_prompt_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "prompts", f"{stage}_stage_decoding_prompt.txt")
            decoding_prompt_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "prompts", f"{problem}_{stage}_stage_decoding_prompt.txt")
            with open(decoding_prompt_file_path, 'w') as file:
                file.write(decoding_prompt)

        return code_decodings, task_decoded_codes
        # return code_decodings, code_file_path_list
    
    def gen_classifier_outputs(self, problem_file_path_list, classifier_prompt, pseudocode_encoding_list, stage, timestamp, it, round, client):
        message_list = []
        for pseudocode in pseudocode_encoding_list:
            message=[
                {
                    "role": "user",
                    "content": classifier_prompt + "\nPseudocode:" +  pseudocode,
                }
            ]
            message_list.append(message)
        output_responses = client.multi_chat_completion(message_list)

        # Write codes to file:
        output_list = []
        for idx in range(len(output_responses)):
            decoding = output_responses[idx]
            code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
            code = textwrap.dedent(code_blocks[0])
            result = int(code)
            output_list.append(result)


        return output_list
    
    def process_single_problem(self, problem, problem_file_path, code_solution_path, pseudocode_encoding, timestamp, iter, stage):
        # print(f"Processing {problem}", flush=True)
        # return problem, {"metric": 1.0}, ([1.0], None)
        # print('in process_single_problem')
        # problem_file_path = os.path.join(src_dir, dataset_name, problem)
        # list_of_instance = load_data(file_path)
        # inst_total = len(list_of_instance)
        unsafe_execute()
        num_test_cases = get_num_test_cases(problem_file_path)
        # print(f'inst_total in process_single_problem(): {inst_total}', flush=True)
        instance_results = [None] * num_test_cases
        # print('empty instance_results: ', instance_results)

        # code_solution_path, pseudocode_encoding = self.get_code_solution(problem_file_path, prompt, prev_stage_prompt, timeout, stage, timestamp, it, round, client)
        # print(f'code_solution_path: {code_solution_path}', flush=True)
        # print(f'pseudocode_encoding: {pseudocode_encoding}', flush=True)
        # print('pseudocode_encoding: ', pseudocode_encoding)
        metrics = get_metrics(pseudocode_encoding)
        # print('metrics: ', metrics)
        if metrics == None:
            metrics = {}
        # print(f'metrics in process_single_problem(): {metrics}', flush=True)
        timeout_errors = 0
        for idx in range(num_test_cases):
            # print('is this for loop even being run?')
            try: 
                # result = 1 #[TO DO]: change to below, and pass in timstamp, iter, round, stage
                if timeout_errors < 5:
                    error_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{iter}", "errors", f"error_{idx}_{stage}.txt") # [TO DO]: change!!
                    result, timeout_error = run_test_case(problem_file_path, code_solution_path, idx+1, timestamp, iter, stage, error_file_path) # [TO DO]: check if run_test_case() returns error or exception at some point
                    timeout_errors += timeout_error
                else:
                    result = "Exception: Time Out Error" # if 5 test cases time out, all of them are likely to time out because there's probably a bug in the code
                # print('result in try: ', result)
            except Exception as e:
                result = f"Exception: {str(e)}"
                # print('result in exception: ', result)

            instance_results[idx] = result
        # print('instance_results: ', instance_results)
        return problem, metrics, (instance_results, None) # None refers to no error
    
    def evaluate_jsonl_problems(
            input_file: str, 
            task_decoded_codes: Dict,
            predict_column: str = 'response',
            version: str = 'v0.3.0',
            split: str = 'test',
            ):
        """
        Evaluate the functional correctness of the LeetCoTE problems.
        """
        problem_file = get_problem_file(version, split)
        k = list(map(int, k.split(",")))

        # prepare sample file
        # result = []
        # for sample in read_jsonl(input_file):
        #     assert 'task_id' in sample, f'`task_id` should be specified in {input_file}'
        #     text = get_nested(sample, predict_column)
        #     sample['completion'] = code_extract(text)
        #     result.append(sample)
        # assert '.jsonl' in input_file, 'input_file must be a jsonl file'
        # sample_file = input_file.replace('.jsonl', '_sample.jsonl')
        # write_jsonl(sample_file, result)
        for problem in task_decoded_codes:
            decoded_code = task_decoded_codes[problem]

        results = evaluate_functional_correctness(sample_file, problem_file, k)
        print(results)
    
    def process_all_problems(self, problem_cases, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, client,
                          timeout=60, instance_workers=4, case_workers=4):
        
        problem_file_path_list = [os.path.join(src_dir, dataset_name, problem) for problem in problem_cases]
        # [TO DO]: problem_file_path_list = problem_cases

        results = {}
        metrics = {}
        code_list = []
        if stage == 'encoder': # [TO DO]: can't i juse pass in encoding_prompt and decoding_prompt?
            encoding_prompt = prompt
            decoding_prompt = prev_stage_prompt
            code_list = get_original_codes(problem_file_path_list) # [TO DO]: change
        elif stage == 'decoder':
            encoding_prompt = prev_stage_prompt
            decoding_prompt = prompt

        
        # print('case workers: ', case_workers)
        # print('instance_workers: ', instance_workers)
        # print('problem_cases in process_all_problems: ', problem_cases)
        pseudocode_encoding_list = self.gen_multi_chat_encodings(dataset_name, problem_file_path_list, encoding_prompt, stage, timestamp, it, client)
        # code_decoding_list, code_file_path_list = self.gen_multi_chat_decodings(dataset_name, problem_cases, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, client)
        code_decoding_list, task_decoded_codes = self.gen_multi_chat_decodings(dataset_name, problem_cases, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, client)
        if stage == 'decoder':
            code_list = code_decoding_list
        pbar = tqdm(total=len(problem_cases), desc=f"Processing cases for '{dataset_name}'", unit="case")
        print('in process_all_problems()')
        for idx, problem in enumerate(problem_cases):
            problem_file_path = problem_file_path_list[idx]
            code_solution_path = code_file_path_list[idx]
            pseudocode_encoding = pseudocode_encoding_list[idx]

            # print('problem: ', problem)
            # print('code solution path: ', code_solution_path)
            # print('pseudocode encoding: ', pseudocode_encoding)
            try:
                # print('right before getting result() in try case:')                
                problem_case, problem_metrics, case_result = self.process_single_problem(problem, problem_file_path, code_solution_path, pseudocode_encoding, timestamp, it, stage)
                # print('problem metrics: ', problem_metrics)
                # print('case result: ', case_result)
                # print('problem_case: ', problem_case)
                # print('problem_metrics: ', problem_metrics)
                # print('case_result: ', case_result)
            except Exception as e:
                problem_case = problem
                case_result = (None, f"Exception: {str(e)}")
                problem_metrics = None # [TO DO]: in normalize_metrics() and average_metrics(), check for when metrics is none
            # print('case result: ', case_result)
            results[problem_case] = case_result
            metrics[problem_case] = problem_metrics
            pbar.update(1)
        pbar.close()

        return results, metrics, pseudocode_encoding_list, code_list
    
    def process_all_problems_classifier(self, problem_cases, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, round, client,
                          timeout=60, instance_workers=4, case_workers=4):
        results = {}
        metrics = {}
        if stage == 'encoder': # [TO DO]: can't i juse pass in encoding_prompt and decoding_prompt?
            encoding_prompt = prompt
            decoding_prompt = prev_stage_prompt
        elif stage == 'decoder':
            encoding_prompt = prev_stage_prompt
            decoding_prompt = prompt

        problem_file_path_list = [os.path.join(src_dir, dataset_name, problem) for problem in problem_cases]
        # print('case workers: ', case_workers)
        # print('instance_workers: ', instance_workers)
        # print('problem_cases in process_all_problems: ', problem_cases)
        # output_list = self.gen_classifier_outputs()
        pseudocode_encoding_list = self.gen_multi_chat_encodings(problem_file_path_list, encoding_prompt, stage, timestamp, it, round, client)
        code_file_path_list = self.gen_multi_chat_decodings(problem_file_path_list, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, round, client)
        pbar = tqdm(total=len(problem_cases), desc=f"Processing cases for '{dataset_name}'", unit="case")
        print('in process_all_problems()')
        for idx, problem in enumerate(problem_cases):
            problem_file_path = problem_file_path_list[idx]
            code_solution_path = code_file_path_list[idx]
            pseudocode_encoding = pseudocode_encoding_list[idx]

            # print('problem: ', problem)
            # print('code solution path: ', code_solution_path)
            # print('pseudocode encoding: ', pseudocode_encoding)
            try:
                # print('right before getting result() in try case:')                
                problem_case, problem_metrics, case_result = self.process_single_problem(problem, problem_file_path, code_solution_path, pseudocode_encoding, timestamp, it, round, stage)
                # print('problem metrics: ', problem_metrics)
                # print('case result: ', case_result)
                # print('problem_case: ', problem_case)
                # print('problem_metrics: ', problem_metrics)
                # print('case_result: ', case_result)
            except Exception as e:
                problem_case = problem
                case_result = (None, f"Exception: {str(e)}")
                problem_metrics = None # [TO DO]: in normalize_metrics() and average_metrics(), check for when metrics is none
            # print('case result: ', case_result)
            results[problem_case] = case_result
            metrics[problem_case] = problem_metrics
            pbar.update(1)
        pbar.close()
        return results, metrics

    def __call__(self, problem_cases, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, client, 
                          timeout=60, instance_workers=4, case_workers=4):
        # return self.process_all_problems(problem_cases, dataset_name, load_data, solve_source, prev_stage_prompt, client, config_path, src_dir, stage)
        return self.process_all_problems(problem_cases, dataset_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, client,
                            timeout, case_workers, instance_workers)


def filter_dev(results, dev):
    if dev is None:
        return results
    dev_results = {}
    for case, (scores, error_message) in results.items():
        if case not in dev:
            continue
        dev_list = dev[case]
        if len(dev_list) == 0:
            dev_list = [0]
        select_scores = []
        for idx, score in enumerate(scores):
            if idx in dev_list:
                select_scores.append(score)
        if len(select_scores) > 0:
            dev_results[case] = (select_scores, error_message)
    return dev_results


def filter_test(results, dev):
    if dev is None:
        return results
    test_results = {}
    for case, (scores, error_message) in results.items():
        if case not in dev:
            test_results[case] = (scores, error_message)
            continue
        dev_list = dev[case]
        if len(dev_list) == 0:
            dev_list = [0]
        select_scores = []
        for idx, score in enumerate(scores):
            if idx not in dev_list:
                select_scores.append(score)
        if len(select_scores) > 0:
            test_results[case] = (select_scores, error_message)
    return test_results


def eval_all(results, test_cases):
    return sum(
        (sum(x if not isinstance(x, str) else 0 for x in scores) / len(scores)
         if not error_message else 0)
        for scores, error_message in (results.get(problem_case, (None, "No result")) for problem_case in results.keys())
    ) / len(results)

def get_problem_passing_rates(results):
    problem_scores = {}
    for problem_case in results.keys():
        scores, error_message = results.get(problem_case, (None, "No result")) 
        if not error_message:
            problem_scores[problem_case] = sum(x if not isinstance(x, str) else 0 for x in scores) / len(scores)
        else:
            problem_scores[problem_case] = 0
    return problem_scores

def compare_results(results, reference_results, test_cases):
    imp = dec = tie = 0
    for case in test_cases:
        new, new_err = results.get(case, (None, "No result"))
        ref, ref_err = reference_results.get(case, (None, "No result"))
        new_avg = sum(x if not isinstance(x, str) else 0 for x in new) / len(new) if not new_err else 0
        ref_avg = sum(x if not isinstance(x, str) else 0 for x in ref) / len(ref) if not ref_err else 0
        imp, dec, tie = (imp + 1, dec, tie) if new_avg > ref_avg else (imp, dec + 1, tie) if new_avg < ref_avg else (
        imp, dec, tie + 1)
    return imp, dec, tie


def extract_code_blocks(response):
    pattern_backticks = r"```python\s*(.*?)\s*```"
    pattern_dashes = r"^-{3,}\s*\n(.*?)\n-{3,}"
    blocks = re.findall(pattern_backticks, response, re.DOTALL)
    blocks.extend(re.findall(pattern_dashes, response, re.DOTALL | re.MULTILINE))
    return blocks


# from ReEvo utils.py:
def file_to_string(filename):
    with open(filename, 'r') as file:
        return file.read()
    
# these are the ones i am adding
def get_original_codes(problem_file_path_list):
    original_codes = []
    for problem_file_path in problem_file_path_list:
        code_file_path = os.path.join(problem_file_path, "llm_scripting", "starter_code.py")
        with open(code_file_path, 'r') as file:
            code = file.read()
            original_codes.append(code)

    return original_codes

def get_num_test_cases(problem_file_path):
    test_cases_folder = Path(problem_file_path) / "test_cases"
    num_test_cases = sum(1 for item in test_cases_folder.iterdir() if "input" in item.name)
    return num_test_cases

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        # Process each line, split into tokens, and strip unwanted chars
        processed = []
        for line in file:
            processed.extend(token.strip(' (,)') for token in line.split())
        return processed

def compare_outputs(file_path_expected, file_path_stdout):
    list_expected = read_file_to_list(file_path_expected)
    list_stdout = read_file_to_list(file_path_stdout)
    # print("list expected: ", list_expected)
    # print("list stdout: ", list_stdout)
    return list_expected == list_stdout

    # if len(list_expected) != len(list_stdout):
    #     return False
    # # smallest_length = min(len(list_expected), len(list_stdout))
    # for i in range(len(list_expected)):
    #     if list_expected[i] != list_stdout[i]:
    #         return False
        
    # return True

def run_test_case(problem_file_path, code_solution_path, idx, timestamp, iter, stage, error_file_path):
    input_file_path = os.path.join(problem_file_path, "test_cases", f"{idx}_input.txt")
    output_file_path = os.path.join(problem_file_path, "test_cases", f"{idx}_output.txt")
    stdout_file_path = os.path.join(problem_file_path, "outputs", "stdouts", f"{idx}_stdout.txt")
    # error_file_path = f"{problem_path}/outputs/errors/{timestamp}/decoding_prompt_{decoding_prompt_num}_trial_{trial}_test_case_{i}.txt"
    # error_file_path = os.path.join(problem_file_path, "outputs", "errors", timestamp, f"iter_{iter}_error_{idx}_{stage}.txt") # [TO DO]: change!!
    timeout = 5
    num_correct = 0
    num_errors = 0
    timeout_error = 0
    try:

        with open(input_file_path, 'r') as input_file, open(stdout_file_path, 'w') as output_file, open(error_file_path, 'w') as error_file:
            result = subprocess.run(["python3", code_solution_path], stdin=input_file, stdout=output_file, stderr=error_file, timeout=10) #capture stdout and stderr

        # if result.returncode == 0:
        #     print("Script ran successfully.")
        # else:
        #     print("Script failed:", result.stderr)
        if result.returncode != 0:
            print(f"Script failed with return code {result.returncode}. Check the error file at {error_file_path} for details.\n")
            num_errors += 1
            # if num_errors == 2:
            #     break # if there is an error for one trial, there must be an error for the other trials
        else: # delete the file cause it's taking up too much space
            # If the script succeeded, delete the error file
            if os.path.exists(error_file_path):
                os.remove(error_file_path)
                # print(f"Script succeeded. Deleted the error file at {error_file_path}.")

        # Compare the captured output with the contents of the output file
        with open(output_file_path, "r") as f:
            expected_output = f.read()
        if compare_outputs(output_file_path, stdout_file_path):
        # Comparing the result's stdout to the expected output
        # if result.stdout == expected_output:
            # print("Output matches the expected output.")
            num_correct = 1
    except subprocess.TimeoutExpired:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        timeout_error = 1
        with open(error_file_path, 'a') as file:
            file.write(f"Script timed out after {timeout} seconds.")
            file.write("------------------------------------------\n")
        print(f"Script timed out after {timeout} seconds.")
    except subprocess.CalledProcessError as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Script failed with error: {e}")
        with open(error_file_path, 'a') as file:
            file.write("Script failed with error:\n")
            file.write(f"{e}\n")
            file.write("------------------------------------------\n")
    except FileNotFoundError as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Error: {e}")
        with open(error_file_path, 'a') as file:
            file.write("File not found error:\n")
            file.write(f"{e}\n")
            file.write("------------------------------------------\n")
    except Exception as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Unexpected error: {e}")
        with open(error_file_path, 'a') as file:
            file.write("Unexpected error:\n")
            file.write(f"{e}\n")
            file.write("------------------------------------------\n")
    return num_correct, timeout_error

def unsafe_execute(problem: Dict, completion: str, timeout: float, result):
    with create_tempdir():
        import os
        import shutil

        # Backup original functions for cleanup
        rmtree = shutil.rmtree
        rmdir = os.rmdir
        chdir = os.chdir

        reliability_guard()

        # Extract individual test cases by splitting on 'assert' statements
        test_cases = []
        test_code = problem["test"].strip()
        if test_code:
            # Split test cases while preserving assertion lines
            test_lines = test_code.split('\n')
            current_test = []
            for line in test_lines:
                if line.strip().startswith('assert '):
                    if current_test:  # Save previous test case
                        test_cases.append('\n'.join(current_test))
                        current_test = []
                current_test.append(line)
            if current_test:  # Add the last test case
                test_cases.append('\n'.join(current_test))

        # Prepare the base program (prompt + completion)
        base_program = problem["prompt"] + "\n" + completion + "\n"

        test_results = []
        all_passed = True

        for test_case in test_cases:
            check_program = base_program + test_case + "\n"

            try:
                exec_globals = {}
                with swallow_io():
                    with time_limit(timeout):
                        exec(check_program, exec_globals)
                test_results.append({"test_case": test_case, "passed": True, "error": None})
            except TimeoutException:
                test_results.append({"test_case": test_case, "passed": False, "error": "timed out"})
                all_passed = False
                break  # Timeout applies to the whole problem
            except BaseException as e:
                test_results.append({"test_case": test_case, "passed": False, "error": str(e)})
                all_passed = False
                # Continue to next test case (comment this line to stop on first failure)

        # Restore original functions
        shutil.rmtree = rmtree
        os.rmdir = rmdir
        os.chdir = chdir

        if all_passed:
            result.append({"status": "passed", "test_results": test_results})
        else:
            result.append({"status": "failed", "test_results": test_results})

def get_test_cases_jsonl():
    test_cases = []
    test_code = problem["test"].strip()
    if test_code:
        # Split test cases while preserving assertion lines
        test_lines = test_code.split('\n')
        current_test = []
        for line in test_lines:
            if line.strip().startswith('assert '):
                if current_test:  # Save previous test case
                    test_cases.append('\n'.join(current_test))
                    current_test = []
            current_test.append(line)
        if current_test:  # Add the last test case
            test_cases.append('\n'.join(current_test))

def minify_code(problem_file_path, code_solution_path):
    stdout_file_path = os.path.join(problem_file_path, "outputs", "stdouts", f"minified_code.py")
    # error_file_path = f"{problem_file_path}/outputs/errors/{timestamp}/decoding_prompt_{decoding_prompt_num}_trial_{trial}_test_case_{i}.txt"
    timeout = 10
    print('stdout_file_path in minify_code: ', stdout_file_path)
    try:

        with open(stdout_file_path, 'w') as output_file:
            # result = subprocess.run(["python3", code_solution_path], stdout=output_file, timeout=10) #capture stdout and stderr
            result = subprocess.run(["pyminify", "--rename-locals", "--rename-globals", code_solution_path], capture_output=True, text=True, timeout=10)

        with open(stdout_file_path, "w") as f:
            f.write(result.stdout)

        return result.stdout
        # if result.returncode == 0:
        #     print("Script ran successfully.")
        # else:
        #     print("Script failed:", result.stderr)
        # if result.returncode != 0:
            # print(f"Script failed with return code {result.returncode}. Check the error file at {error_file_path} for details.\n")
            # num_errors += 1
            # if num_errors == 2:
            #     break # if there is an error for one trial, there must be an error for the other trials
        # else: # delete the file cause it's taking up too much space
            # If the script succeeded, delete the error file
            # if os.path.exists(error_file_path):
            #     os.remove(error_file_path)
                # print(f"Script succeeded. Deleted the error file at {error_file_path}.")

        # Compare the captured output with the contents of the output file
        # with open(output_file_path, "r") as f:
        #     expected_output = f.read()
        # if compare_outputs(output_file_path, stdout_file_path):
        # Comparing the result's stdout to the expected output
        # if result.stdout == expected_output:
            # print("Output matches the expected output.")
            # num_correct = 1
    except subprocess.TimeoutExpired:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        # with open(error_file_path, 'a') as file:
        #     file.write(f"Script timed out after {timeout} seconds.")
        #     file.write("------------------------------------------\n")
        print(f"Script timed out after {timeout} seconds.")
    except subprocess.CalledProcessError as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Script failed with error: {e}")
        # with open(error_file_path, 'a') as file:
        #     file.write("Script failed with error:\n")
        #     file.write(f"{e}\n")
        #     file.write("------------------------------------------\n")
    except FileNotFoundError as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Error: {e}")
        # with open(error_file_path, 'a') as file:
        #     file.write("File not found error:\n")
        #     file.write(f"{e}\n")
        #     file.write("------------------------------------------\n")
    except Exception as e:
        num_correct = 0 # if faulty code, none of them are going to pass so break
        print(f"Unexpected error: {e}")
    #     with open(error_file_path, 'a') as file:
    #         file.write("Unexpected error:\n")
    #         file.write(f"{e}\n")
    #         file.write("------------------------------------------\n")
    # return num_correct
    return None
# Metrics:

def count_lines(string):
    return len(string.splitlines())

def keyword_count(string):
    keywords=["if", "else", "for", "while", "return"]
    words = string.split()
    keyword_count = sum(1 for word in words if word in keywords)
    return keyword_count if words else 0
    # return keyword_count / len(words) if words else 0 # for keyword_density

def comment_count(string):
    lines = string.splitlines()
    comment_lines = sum(1 for line in lines if line.strip().startswith("#") or "//" in line)
    return comment_lines if lines else 0

def avg_variable_name_length(string):
    # [TO DO]: clean up the regex
    keywords=["if", "else", "for", "while", "return", "in", "with", "open", "range", "str", "int", "float"]
    variables = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', string)
    variables = [word for word in variables if word not in keywords]
    return sum(len(var) for var in variables) / len(variables) if variables else 0

def variable_count(string):
    keywords=["if", "else", "for", "while", "return", "in", "with", "open", "range", "str", "int", "float"]
    variables = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', string)
    variables = [word for word in variables if word not in keywords]
    return len(variables) if variables else 0


def count_functions(string):
    return string.lower().count("function") + string.lower().count("procedure")

def word_count(string):
    return len(string.split())

def char_count(string):
    words = string.split()
    return sum( len(word) for word in words)

# def is_pseudocode_natural(code_line):
def avg_word_length(code_string):
    words = code_string.split()
    
    # Check for technical operators
    # technical_symbols = {"++", "--", "+=", "-=", "*=", "/=", "="}
    # if any(symbol in code_line for symbol in technical_symbols): [TO DO]: penalize this somehow in the avg word length
    #     return False
    
    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Check if words are sufficiently long (e.g., avg >= 4)
    return avg_word_length
    # return avg_word_length >= 4.0

def avg_syllables_per_word(text):
    dic = pyphen.Pyphen(lang='en')
    words = text.split()
    syllable_counts = [len(dic.inserted(word).split('-')) for word in words]
    return sum(syllable_counts) / len(words) if words else 0

    # See below: do I want to use a threshold? where i keep redoing the prompt until i get a score that crosses the threshold?

# def is_pseudocode_complex(code_line):
#     if any(sym in code_line for sym in {"++", "--", "+=", "="}):
#         return False
#     return avg_syllables_per_word(code_line) >= 1.5  # Adjust threshold
def syllable_count(text):
    dic = pyphen.Pyphen(lang='en')
    words = text.split()
    syllable_counts = [len(dic.inserted(word).split('-')) for word in words]
    return sum(syllable_counts)

def pseudocode_readability(text):
    # Higher score = easier to read (more natural)
    return textstat.flesch_reading_ease(text) # or should i do a threshold below?
    # return textstat.flesch_reading_ease(text) > 60  # Adjust threshold

def add_metrics(new_metrics_dict, old_metrics_dict):
    for key, value in new_metrics_dict.items():
        if key not in old_metrics_dict:
            old_metrics_dict[key] = new_metrics_dict[key]
        else:
            old_metrics_dict[key] += new_metrics_dict[key]

    return old_metrics_dict

def get_metrics(pseudocode): #remove 'classifier_label' parameter for now
    # am going to remove the parameter 'metrics_path' for now

    metrics = {
        "line_count": count_lines(pseudocode),
        "keyword_count": keyword_count(pseudocode),
        "comment_count": comment_count(pseudocode),
        "avg_variable_name_length": avg_variable_name_length(pseudocode),
        "word_count": word_count(pseudocode),
        "line_length": calculate_reward_pseudocode(pseudocode),
        "avg_word_length": avg_word_length(pseudocode),
        "avg_syllables_per_word": avg_syllables_per_word(pseudocode),
        "syllable_count": syllable_count(pseudocode),
        "readability": pseudocode_readability(pseudocode),
        # "char_count": char_count(original_code),
        # "max_num_test_cases_passed" : num_test_cases,
        # "max_passing_rate" : max_num_test_cases_passed/num_test_cases,
    }

    # if stage == "code":
    #     # difference_metrics["max_num_test_cases_passed"] = final_metrics["max_num_test_cases_passed"]
    #     metrics["max_passing_rate"] = max_num_test_cases_passed/num_test_cases
    return metrics

def normalize_metrics(metrics):
    # metrics is a dictionary with problem names being the keys and the pseudocode metrics for each problem being the value
    metrics_min_max = {}
    new_dataset_dict = {}
    problem_count = 0
    # Step 1: get the minimums and maximums of everything
    for problem_name_key, metrics_dict in metrics.items():
        problem_count += 0 
        for metric_key in metrics_dict:
            metric_value = metrics_dict[metric_key]

            if metric_key not in metrics_min_max:
                min_max_list = [metric_value, metric_value]
                metrics_min_max[metric_key] = min_max_list
            else:
                metric_min = metrics_min_max[metric_key][0]
                metric_max = metrics_min_max[metric_key][1]
            

                if metric_value < metric_min:
                    metrics_min_max[metric_key][0] = metric_value
                elif metric_value > metric_max:
                    metrics_min_max[metric_key][1] = metric_value

    # Step 2: use min and maxes to apply normalization formula
    for problem_name_key, metrics_dict in metrics.items():
        new_metrics_dict = {}
        for metric_key in metrics_dict:
            metric_value = metrics_dict[metric_key]
            x_min = metrics_min_max[metric_key][0]
            x_max = metrics_min_max[metric_key][1]
            if (x_max - x_min) != 0: 
                normalized_value = (metric_value - x_min)/ (x_max - x_min)
            else:
                normalized_value = 0 # [TO DO]: check if this is right
            new_metrics_dict[metric_key] = normalized_value
        # print('in normalize_metrics:')
        # print(f'problem: {problem_name_key} has dict: {new_metrics_dict}')
        new_dataset_dict[problem_name_key] = new_metrics_dict

    return new_dataset_dict

def average_metrics(normalized_metrics):
    '''
    Average the metrics across all problems. Returns a simple metrics dict where the keys are the metrics and the values are numbers
    '''
    problem_count = 0 
    new_metrics_dict = {}

    for problem_name_key, metrics_dict in normalized_metrics.items():
        problem_count += 1
        for metric_key in metrics_dict:
            metric_value = metrics_dict[metric_key]
            # print(f"for problem name {problem_name_key}, {metric_key} is: {metric_value}")
            if metric_key not in new_metrics_dict:
                new_metrics_dict[metric_key] = metric_value
            else:
                new_metrics_dict[metric_key] += metric_value

    # print('new_metrics_dict: ', new_metrics_dict)

    avgeraged_metrics_dict = {key : value / problem_count for key, value in new_metrics_dict.items()}
    # print("average_metrics_dict: ", avgeraged_metrics_dict)

    return avgeraged_metrics_dict

def save_metrics(avg_metrics, metrics_path, timestamp, stage, iteration):
    metrics_file_path = f'{metrics_path}/{timestamp}_metrics.json' # [TO DO]: create time stamp directory, refactor calculate_metrics i think to only do encoding or decoding metrics
    # metrics_file_path = f'{metrics_path}/{timestamp}_encoder_metrics.json'
    # Load existing data (if any)
    if os.path.exists(metrics_file_path):
        with open(metrics_file_path, "r") as f:
            results = json.load(f)
    else:
        results = []

    new_result = {key: value for key, value in avg_metrics.items()}
    # new_result['iteration-rounds'] = (iteration * (rounds + 1)) + round
    new_result['iter'] = iteration
    # new_result['round'] = round
    new_result['stage'] = stage

    # if round == rounds: ## means one iterations # [TO DO]: add a new condition here

        # Append new result
    results.append(new_result)

    # Save updated results
    with open(metrics_file_path, "w") as f:
        json.dump(results, f, indent=2)  # `indent` for readability

def check_if_no_metrics(metrics):
    metric_keys = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "avg_word_length", "avg_score"]
    new_metrics_dict = {}

    for problem_name_key, metrics_dict in metrics.items():
        if metrics_dict is None:
            new_metrics_dict[problem_name_key] = {metric_key: 0 for metric_key in metric_keys}
        else:
            new_metrics_dict[problem_name_key] = metrics_dict
    return new_metrics_dict

def get_problem_readability_scores(problem_metrics, metric_key):
    metric_keys = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "avg_word_length", "avg_score"]
    new_metrics_dict = {}

    for problem_name_key, metrics_dict in problem_metrics.items():
        metric_value = metrics_dict[metric_key]
        new_metrics_dict[problem_name_key] = metric_value
    return new_metrics_dict

def record_problem_scores(problem_scores, avg_metrics, metric):
    for problem, score in problem_scores.items():
        avg_metrics[problem + f"_{metric}"] = score
    return avg_metrics

def save_prompt(generated_prompts_path, prompt, it, stage):
    file_name = os.path.join(generated_prompts_path, f'prompt_iter_{it}_{stage}.txt' )
    with open(file_name, 'w') as file:
        file.write(prompt)

def calculate_reward_pseudocode(pseudocode):
    lines = pseudocode.split('\n')
    num_lines = len(lines)
    total_length = sum(len(line.strip()) for line in lines)
    
    # ine length threshold - adjust depending on dataset
    min_desired_length = 6  
    
    # Reward for longer lines (if line length > threshold)
    line_length_reward = sum(
        max(0, len(line.strip()) - min_desired_length)
        for line in lines
    )
    
    # Penalty if too few lines (to prevent single-line collapse)
    min_desired_lines = 5  # Adjust based on need
    line_count_penalty = max(0, min_desired_lines - num_lines) * 2  # Arbitrary penalty factor
    
    # Normalize reward by number of lines (avoid excessive reward for many short lines)
    normalized_reward = line_length_reward / num_lines
    
    # Final reward: balance length reward and line count penalty
    final_reward = normalized_reward - line_count_penalty
    
    return final_reward

def get_pseudocode_dataset(json_path_name, problems_dir, timestamp, stage):
    # First step: go into the metrics json file and see which iter rounds have a score of 1.0 and which don't.
    # so in the pandas dataframe we have the following columns: problem, pseudocode, score
    # i guess that begs the other question of how many examples to have per problem? i guess just one for now.
    problems_dir_path = Path(problems_dir)
    problems = {problem.name for problem in problems_dir_path.iterdir() if problem.is_dir() and problem.name != 'metrics'}
    num_problems = len(problems)
    positive_problems = set()
    negative_problems = set()
    positive_examples = []
    negative_examples = []
    with open(json_path_name, 'r') as file:
        data = json.load(file)

    # Now 'data' is a Python list containing your dictionary
    # print(data)

    dataset_list = []

    # First step: get the iters and rounds of the pseudocodes, now we gotta go find the pseudocodes
    for i in range(len(data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
        entry = data[i]
        for problem in problems:
            if entry[problem] == 1.0 and problem not in positive_problems:
                positive_examples.append({"problem":problem, "score": 1.0, "iter": entry["iter"], "round": entry["round"]})
                positive_problems.add(problem)
            elif entry[problem] != 1.0 and problem not in negative_problems:
                negative_examples.append({"problem":problem, "score": 0, "iter": entry["iter"], "round": entry["round"]})
                negative_problems.add(problem)
        if len(positive_problems) == num_problems and len(negative_problems) == num_problems:
            break

    # Second step: find the pseudocodes
    final_positive_examples = []
    final_negative_examples = []
    for entry in positive_examples:
        # print('entry:')
        # print(entry)
        problem = entry["problem"]
        iter = entry["iter"]
        round = entry["round"]
        score = entry["score"]

        pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_round_{round}_pseudocode_{stage}.txt")

        with open(pseudocode_path_name, 'r') as file:
            pseudocode = file.read()
        
        final_positive_examples.append({"problem":problem, "score": score, "pseudocode": pseudocode})

    for entry in negative_examples:
        # print('entry:')
        # print(entry)
        problem = entry["problem"]
        iter = entry["iter"]
        round = entry["round"]
        score = entry["score"]

        pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_round_{round}_pseudocode_{stage}.txt")

        with open(pseudocode_path_name, 'r') as file:
            pseudocode = file.read()
        
        final_negative_examples.append({"problem":problem, "score": score, "pseudocode": pseudocode})

    print('length of positive examples: ', len(final_positive_examples))
    print('length of negative examples: ', len(final_negative_examples))

    
    return final_positive_examples, final_negative_examples

def gen_classifier_outputs(pseudocode_encoding_list, classifier_prompt, client):
        message_list = []
        for pseudocode in pseudocode_encoding_list:
            message=[
                {
                    "role": "user",
                    "content": classifier_prompt + "\nPseudocode:" +  pseudocode,
                }
            ]
            message_list.append(message)
        output_responses = client.multi_chat_completion(message_list)

        print('output_responses: ', output_responses)

        # Write codes to file:
        output_list = [int(entry.strip('\n`')) for entry in output_responses]
        # for idx in range(len(output_responses)):
        #     decoding = output_responses[idx]
        #     code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
        #     code = textwrap.dedent(code_blocks[0])
        #     result = int(code)
        #     output_list.append(result)


        return output_list

def evaluate_classifier_prompt(positive_examples, negative_examples, prompt, client):
    # Decide whcih problems to feed to the prompt, first half of the positive examples and first half of the negative examples
    # train_pseudocodes_dataset = positive_examples[:len(positive_examples)//2] + negative_examples[:len(negative_examples)//2]
    train_pseudocodes_dataset = positive_examples + negative_examples
    # print('train_pseudocodes_dataset:', train_pseudocodes_dataset)

    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    pseudocodes = []

    score = 0

    for entry in train_pseudocodes_dataset:
        pseudocodes.append(entry['pseudocode'])

    # print('len of pseudocodes: ', len(pseudocodes))

    # Feed problems to prompt
    output_list = gen_classifier_outputs(pseudocodes, prompt, client)

    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    # print('len of output_list: ', len(output_list))

    # See if the outputs correspond to the actual labels
    for i in range(len(train_pseudocodes_dataset)):
        entry = train_pseudocodes_dataset[i]
        label = entry["score"]
        output = output_list[i]

        if label == output:
            score += 1

    return score

def save_classifier_score(score, metrics_path, timestamp, stage, iteration, round, rounds):
    metrics_file_path = f'{metrics_path}/{timestamp}_{stage}_metrics.json' # [TO DO]: create time stamp directory, refactor calculate_metrics i think to only do encoding or decoding metrics
    # metrics_file_path = f'{metrics_path}/{timestamp}_encoder_metrics.json'
    # Load existing data (if any)
    if os.path.exists(metrics_file_path):
        with open(metrics_file_path, "r") as f:
            results = json.load(f)
    else:
        results = []

    # new_result = {key: value for key, value in avg_metrics.items()}
    new_result = {}
    new_result['iteration-rounds'] = (iteration * (rounds + 1)) + round
    new_result['iter'] = iteration
    new_result['round'] = round
    new_result['score'] = score

    # if round == rounds: ## means one iterations # [TO DO]: add a new condition here

        # Append new result
    results.append(new_result)

    # Save updated results
    with open(metrics_file_path, "w") as f:
        json.dump(results, f, indent=2)  # `indent` for readability