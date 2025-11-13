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
# import psutil
import signal
import subprocess
import os
import signal
import multiprocessing as mp
import fcntl
import pyphen
import textstat
import asyncio
import sacrebleu
import random
from pathlib import Path
from openai import OpenAI
from typing import Dict, Optional
# import nltk
# from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# import cloudpickle
from multiprocessing.reduction import ForkingPickler
from utils.llm_client.base import BaseClient
from evaluation.eval_dataset.evaluate import evaluate_functional_correctness
from evaluation.eval_dataset.data import read_jsonl, write_jsonl


# Use cloudpickle to support pickling dynamic functions.
# ForkingPickler.dumps = cloudpickle.dumps

# nltk.download('punkt')



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

def list_jsonl_task_ids(path=".", split='', version=''):
    task_ids = []

    # jsonl_files = [file for file in os.listdir(path) if (file.endswith('.jsonl') and "train" in file)]
    # filename = os.path.join(path, jsonl_files[0])
    # with open(path, 'r') as f:
    #     lines = f.readlines()
    #     print(f"Total lines in file: {len(lines)}")
    #     for i, line in enumerate(lines, 1):
    #         print(f"Line {i}: {repr(line)}")
    
    # # Then try to parse with error handling
    # for i, problem in enumerate(read_jsonl(path), 1):
    #     print(f'Problem {i} in list_jsonl_task_ids:')
    #     print(problem)
    #     task_id = problem["task_id"]
    #     task_ids.append(task_id)
    # with open(path, 'r') as f:
    #     for i, line in enumerate(f, 1):
    #         line = line.strip()
    #         if not line:  # Skip empty lines
    #             continue
    #         try:
    #             yield json.loads(line)
    #         except json.JSONDecodeError as e:
    #             print(f"Error parsing JSON on line {i}: {line}")
    #             print(f"Error details: {e}")
    #             raise
    for problem in read_jsonl(path):
        # print('problem in list_jsonl_task_ids:')
        # print(problem)
        task_id = problem["task_id"]
        task_id = task_id.replace("/", "-")
        task_ids.append(task_id)
        
    # filename = path
    # with open(filename, 'r', encoding='utf-8') as f:
    #     for line in f:
    #         json_obj = json.loads(line.strip())
    #         task_ids.append(json_obj.get("task_id")) #returns 'None' if "name" doesn't exist

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
        return []
        # unit_test_idx = idx + 1 # add 1 because inputs and outputs for unit tests are not 0-indexed
        # queue = mp.Queue()
        # p = mp.Process(target=self.evaluate_instance_in_subprocess,
        #                args=(unit_test_idx, code_solution_path, problem_file_path, config_path, queue))
        # p.start()

        # Add the process to the cgroup
        # subprocess.run(["cgclassify", "-g", f"cpu,memory:/{cgroup_name}", str(p.pid)],
        #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # p.join(timeout + 1)  # 1 extra second
        # if p.is_alive():
        #     p.terminate()
        #     try:
        #         parent = psutil.Process(p.pid)
        #         it = 1
        #         for child in parent.children(recursive=True):
        #             if it > 100:
        #                 break
        #             child.kill()
        #             it += 1
        #         parent.kill()
        #     except psutil.NoSuchProcess:
        #         pass
        #     p.join(1)
        #     # Kill all processes in the cgroup (including detached pulp solvers)
        #     # subprocess.run(["cgdelete", "-g", f"cpu,memory:/{cgroup_name}"],
        #     #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #     return f"Timeout ({timeout}s)"
        # else:
        #     try:
        #         result = queue.get_nowait()
        #     except Exception:
        #         result = "No result"
        #     # subprocess.run(["cgdelete", "-g", f"cpu,memory:/{cgroup_name}"],
        #     #                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #     return result
        
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
    
    # async def batch_multi_chat_completion_async(client, list_of_messages):
    #     batch_size = 20
    #     all_results = []
        
    #     for i in range(0, len(list_of_messages), batch_size):
    #         batch = list_of_messages[i:i + batch_size]
    #         results = await client.multi_chat_completion_async(batch)
    #         all_results.extend(results)
    #         await asyncio.sleep(1)  # Rate limiting between batches
        
    #     await client.close()


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

    def gen_multi_chat_encodings_cosmetic(self, dataset_name, problems_file_path, encoding_prompt, stage, timestamp, it, client):
        message_list = []

        #[TO DO]: I think actually problem_file_path_list should be the path to the json file. cause i don't think it makes
        # much sense to pass in the task_ids... right? i am going to have to iterate through the jsonl file anyway.
        task_ids = []
        # jsonl_files = [file for file in os.listdir(dataset_name) if file.endswith('.jsonl')]
        # filename = os.path.join(dataset_name, jsonl_files[0])
        original_pseudocodes = []
        encoding_prompt_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "prompts", f"{stage}_stage_encoding_prompt.txt")
        with open(encoding_prompt_file_path, 'w') as file: 
            file.write(encoding_prompt)

        with open(problems_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                json_obj = json.loads(line.strip())
                pseudocode = json_obj.get("pseudocode")
                original_pseudocodes.append(pseudocode)
                    
                task_id = json_obj.get("task_id")
                task_ids.append(task_id)


        # for problem_file_path in problem_file_path_list:
        #     starter_code_path = os.path.join(problem_file_path, "llm_scripting", "starter_code.py")
        #     starter_code = file_to_string(starter_code_path)
                new_task_id = task_id.replace("/", "-")

                # minified_code = minify(starter_code, rename_locals=True, remove_annotations=True, remove_literal_statements=True)
                # description_path = os.path.join(problem_file_path,"description", "description.txt")
                # description = file_to_string(description_path)

                message=[
                    {
                        "role": "user",
                        # "content": encoding_prompt + "\nProblem Description:" +  description + "\nUse this class and function structure to write the pseudocode  :\n" + starter_code,
                        "content": encoding_prompt + "\nPseudocode to create another version of:" +  pseudocode,
                    }
                ]
                message_list.append(message)
            pseudocode_encoding_list = client.multi_chat_completion(message_list)
            # pseudocode_encoding_list = client.multi_chat_completion_batch(message_list)
            # pseudocode_encoding_list = await self.batch_multi_chat_completion_async(client, message_list)
        
        

        # Write pseudocodes to file
        problem_metrics = {}
        # pseudocode_encoding_dict = {}
        # for idx, problem_file_path in enumerate(problem_file_path_list):
        for idx, task_id in enumerate(task_ids):
            modified_pseudocode = pseudocode_encoding_list[idx]
            # pseudocode_encoding_dict[task_id] = pseudocode
            reference = original_pseudocodes[idx]
            bleu_score = pseudocode_bleu_score(reference, modified_pseudocode, verbose=False)
            # metrics = get_metrics(pseudocode)
            problem_metrics[task_id] = {"bleu_score": bleu_score}
            new_task_id = task_id.replace("/", "-")
            # pseudocode_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "pseudocodes", f"pseudocode_{stage}.txt")
            pseudocode_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "pseudocodes", f"{new_task_id}_pseudocode_{stage}.txt")
            with open(pseudocode_file_path, 'w') as file:
                file.write(modified_pseudocode)
    
        return pseudocode_encoding_list, problem_metrics
    
    def gen_multi_chat_encodings(self, dataset_name, problems_file_path, encoding_prompt, stage, timestamp, it, client):
        message_list = []

        #[TO DO]: I think actually problem_file_path_list should be the path to the json file. cause i don't think it makes
        # much sense to pass in the task_ids... right? i am going to have to iterate through the jsonl file anyway.
        task_ids = []
        # jsonl_files = [file for file in os.listdir(dataset_name) if file.endswith('.jsonl')]
        # filename = os.path.join(dataset_name, jsonl_files[0])
        encoding_prompt_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "prompts", f"{stage}_stage_encoding_prompt.txt")
        with open(encoding_prompt_file_path, 'w') as file: 
            file.write(encoding_prompt)

        with open(problems_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                json_obj = json.loads(line.strip())
                if 'human_eval' in dataset_name:
                    original_code = json_obj.get("prompt") + json_obj.get("canonical_solution")
                    # description = json_obj.get("meta").get("question_title")
                    # starter_code = json_obj.get("meta").get("lang_code")
                else:
                    # print("'response' in gen_multi_chat_encodingindgs")
                    if 'v0.3.0' in problems_file_path:
                        original_code = json_obj.get("prompt") + json_obj.get("response")
                        # description = json_obj.get("meta").get("question_title")
                        # starter_code = json_obj.get("meta").get("lang_code")
                    else:
                        original_code = json_obj.get("prompt") + extract_code_blocks(json_obj.get("response"))[0]
                        # description = json_obj.get("meta").get("question_title")
                        # starter_code = json_obj.get("meta").get("lang_code")
                    
                task_id = json_obj.get("task_id")
                task_ids.append(task_id)


        # for problem_file_path in problem_file_path_list:
        #     starter_code_path = os.path.join(problem_file_path, "llm_scripting", "starter_code.py")
        #     starter_code = file_to_string(starter_code_path)
                new_task_id = task_id.replace("/", "-")
                

                # minified_code = minify(starter_code, rename_locals=True, remove_annotations=True, remove_literal_statements=True)
                # description_path = os.path.join(problem_file_path,"description", "description.txt")
                # description = file_to_string(description_path)

                message=[
                    {
                        "role": "user",
                        # "content": encoding_prompt + "\nProblem Description:" +  description + "\nUse this class and function structure to write the pseudocode  :\n" + starter_code,
                        "content": encoding_prompt + "\nCode to translate:" +  original_code,
                    }
                ]
                message_list.append(message)
            pseudocode_encoding_list = client.multi_chat_completion(message_list)
            # pseudocode_encoding_list = client.multi_chat_completion_batch(message_list)
            # pseudocode_encoding_list = await self.batch_multi_chat_completion_async(client, message_list)
        
        

        # Write pseudocodes to file
        problem_metrics = {}
        # pseudocode_encoding_dict = {}
        # for idx, problem_file_path in enumerate(problem_file_path_list):
        for idx, task_id in enumerate(task_ids):
            pseudocode = pseudocode_encoding_list[idx]
            # pseudocode_encoding_dict[task_id] = pseudocode
            metrics = get_metrics(pseudocode)
            problem_metrics[task_id] = metrics
            new_task_id = task_id.replace("/", "-")
            # pseudocode_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "pseudocodes", f"pseudocode_{stage}.txt")
            pseudocode_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "pseudocodes", f"{new_task_id}_pseudocode_{stage}.txt")
            with open(pseudocode_file_path, 'w') as file:
                file.write(pseudocode)
    
        return pseudocode_encoding_list, problem_metrics
    
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
        # code_decodings = client.multi_chat_completion_batch(message_list)
        # code_decodings = await self.batch_multi_chat_completion_async(client, message_list)
        # print('code decodings:', code_decodings)
        # print('length of code_decodings: ', len(code_decodings))
        # print('length of pseudocode encodings: ', len(pseudocode_encoding_list))
        decoding_prompt_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "prompts", f"{stage}_stage_decoding_prompt.txt")
        with open(decoding_prompt_file_path, 'w') as file:
            file.write(decoding_prompt)

        # Write codes to file:
        code_file_path_list = []
        task_pseudocodes_codes = {}
        code_decodings_list = []
        # for idx, problem_file_path in enumerate(problem_file_path_list):
        for idx, problem in enumerate(problem_cases):
            decoding = code_decodings[idx]
            pseudocode = pseudocode_encoding_list[idx]
            # pseudocode = pseudocode_encoding_dict[problem]
            code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
            if len(code_blocks) == 0:
                code_blocks = decoding # in case the prompt didn't output ```python``` formatting, is this the best way to do this?
            # print('code blocks in gen_multi_chat_decodings(): ', code_blocks)
            code = textwrap.dedent(code_blocks[0])
            # code = textwrap.dedent(decoding)
            code_decodings_list.append(code)

            new_task_id = problem.replace("/", "-")
            # code_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "decoded_codes", f"generated_code_{stage}.py")
            code_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "decoded_codes", f"{new_task_id}_decoded_code_{stage}.py")
            with open(code_file_path, 'w') as file:
                file.write(code)
            # code_file_path_list.append(code_file_path)
            task_pseudocodes_codes[problem] = {"pseudocode": pseudocode, "decoded_code": code}

            # decoding_prompt_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "prompts", f"{stage}_stage_decoding_prompt.txt")

        return code_decodings_list, task_pseudocodes_codes
        # return code_decodings, code_file_path_list
    
    def gen_classifier_outputs(self, problem_file_path_list, classifier_prompt, pseudocode_encoding_list, stage, timestamp, it, client):
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
        # problem_file = get_problem_file(version, split)
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

        # results = evaluate_functional_correctness(sample_file, problem_file, k)
        # print(results)
    
    def process_all_problems(self, problem_cases, dataset_name, problems_file_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, client,
                          timeout=60, instance_workers=4, case_workers=4):
        
        problem_file_path_list = [os.path.join(src_dir, dataset_name, problem) for problem in problem_cases]
        # print('problem_file_path_list in process_all_problems():')
        # print(problem_file_path_list)
        # [TO DO]: problem_file_path_list = problem_cases
        dataset_name = os.path.join(src_dir, dataset_name)
        problems_file = os.path.join(dataset_name, problems_file_name)

        print('after setting up dataset name and problems file name')

        results = {}
        metrics = {}
        pseudocode_encoding_dict = {}
        code_dict = {}
        original_pseudocodes = {}
        if stage == 'encoder': # [TO DO]: can't i juse pass in encoding_prompt and decoding_prompt?
            encoding_prompt = prompt
            decoding_prompt = prev_stage_prompt
            # code_list = get_original_codes(problem_file_path_list) # [TO DO]: change
            code_dict = get_original_codes_jsonl(dataset_name, problems_file) # [TO DO]: change
            # print('original codes:')
            # print(code_list)
        elif stage == 'decoder':
            encoding_prompt = prev_stage_prompt
            decoding_prompt = prompt
        elif stage == "cosmetic":
            original_pseudocodes = get_original_pseudocodes_jsonl(problems_file)
            encoding_prompt = prompt
            decoding_prompt = prev_stage_prompt
            # print('origianl pseudocodes:')
            # print(original_pseudocodes)

        
        # print('case workers: ', case_workers)
        # print('instance_workers: ', instance_workers)
        # print('problem_cases in process_all_problems: ', problem_cases)
        print('right before calling gen_multi_chat_encodings: ')
        if stage == 'cosmetic':
            pseudocode_encoding_list, problem_metrics = self.gen_multi_chat_encodings_cosmetic(dataset_name, problems_file, encoding_prompt, stage, timestamp, it, client)
        else:
            pseudocode_encoding_list, problem_metrics = self.gen_multi_chat_encodings(dataset_name, problems_file, encoding_prompt, stage, timestamp, it, client)
        print('after calling gen_multi_chat_encodings')
        # code_decoding_list, code_file_path_list = self.gen_multi_chat_decodings(dataset_name, problem_cases, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, client)
        code_decoding_list, task_pseudocodes_codes = self.gen_multi_chat_decodings(dataset_name, problem_cases, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, client)
        print('after calling gen_multi_chat_decodings')
        # print('code_decoding_list:')
        # for code_dec in code_decoding_list:
        #     print(code_dec)
        #     print('\n')
        code_decoding_dict = {}
        if stage == 'cosmetic':
            for problem in task_pseudocodes_codes.keys():
                pseudocode_encoding_dict[problem] = task_pseudocodes_codes[problem]["pseudocode"]
        else:
            for problem in task_pseudocodes_codes.keys():
                pseudocode_encoding_dict[problem] = task_pseudocodes_codes[problem]["pseudocode"]
                code_decoding_dict[problem] = task_pseudocodes_codes[problem]["decoded_code"]

        if stage == 'decoder':
            code_dict = code_decoding_dict
        pbar = tqdm(total=len(problem_cases), desc=f"Processing cases for '{dataset_name}'", unit="case")
        print('in process_all_problems()')

        # [TO DO]: figure out how to do metrics in evaulaute_functional_correctness()
        # [TO DO]: figure out how to do the same case_result structure..
        # [TO DO]: figure out how to do errors, like where to print them to.
        # [TO DO]: should the problem_metrics include the passing rate??
        # for idx, problem in enumerate(problem_cases):
        #     problem_file_path = problem_file_path_list[idx]
        #     code_solution_path = code_file_path_list[idx]
        #     pseudocode_encoding = pseudocode_encoding_list[idx]
        #     try:
        #         problem_case, problem_metrics, case_result = self.process_single_problem(problem, problem_file_path, code_solution_path, pseudocode_encoding, timestamp, it, stage)

        #     except Exception as e:
        #         problem_case = problem
        #         case_result = (None, f"Exception: {str(e)}")
        #         problem_metrics = None # [TO DO]: in normalize_metrics() and average_metrics(), check for when metrics is none

        #     results[problem_case] = case_result
        #     metrics[problem_case] = problem_metrics
        #     pbar.update(1)
        # pbar.close()
        error_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "errors")
        num_errors = 2
        results, errors = evaluate_functional_correctness(dataset_name, problems_file, task_pseudocodes_codes)
        write_errors_to_file(error_file_path, errors, num_errors)
        # print('results from evaluate_functional_correctness:')
        # print(results)
        if stage == 'cosmetic':
            return results, problem_metrics, original_pseudocodes, pseudocode_encoding_dict, errors
        else:
            return results, problem_metrics, pseudocode_encoding_dict, code_dict, errors
    
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

    def __call__(self, problem_cases, dataset_name, problems_file_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, client, 
                          timeout=60, instance_workers=4, case_workers=4):
        # return self.process_all_problems(problem_cases, dataset_name, load_data, solve_source, prev_stage_prompt, client, config_path, src_dir, stage)
        return self.process_all_problems(problem_cases, dataset_name, problems_file_name, prompt, prev_stage_prompt, config_path, src_dir, stage, timestamp, it, client,
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
         if (not error_message and scores) else 0)
        for scores, error_message in (results.get(problem_case, (None, "No result")) for problem_case in results.keys())
    ) / len(results) if results else 0

def get_problem_passing_rates(results):
    problem_scores = {}
    for problem_case in results.keys():
        scores, error_message = results.get(problem_case, (None, "No result")) 
        if not error_message and scores:
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
def get_original_codes_jsonl(dataset_name, problems_file):
    original_codes = {}
    for problem in read_jsonl(problems_file):
        # task_id = problem["task_id"]
        print('dataset_name: ', dataset_name)
        if 'human_eval' in dataset_name:
            code = problem["canonical_solution"]
        else:
            print("response in get_original_codes_jsonl")
            if "v0.3.0" in problems_file:
                code = problem["response"]
            else:
                code = extract_code_blocks(problem["response"])[0]
            
        original_codes[problem["task_id"]] = code
    return original_codes

def get_original_pseudocodes_jsonl(problems_file):
    original_pseudocodes = {}
    for problem in read_jsonl(problems_file):
        # task_id = problem["task_id"]
        pseudocode = problem["pseudocode"]
            
        original_pseudocodes[problem["task_id"]] = pseudocode
    return original_pseudocodes

def get_original_codes(problem_file_path_list): # [TO DO]: change original_codes to Dict to keep track of task_ids with their codes
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
    words = re.findall(r'\b\w+\b', code_string)
    
    # Check for technical operators
    # technical_symbols = {"++", "--", "+=", "-=", "*=", "/=", "="}
    # if any(symbol in code_line for symbol in technical_symbols): [TO DO]: penalize this somehow in the avg word length
    #     return False
    
    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
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

def avg_words_per_line(pseudocode):
    lines = pseudocode.strip().splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    total_words = 0
    total_lines = len(lines)
    
    for line in lines:
        words_in_line = re.findall(r'\b\w+\b', line)  # Split by word boundaries
        total_words += len(words_in_line)
    
    avg_words_per_line = total_words / total_lines if total_lines > 0 else 0

    return avg_words_per_line

def pseudocode_bleu_score(reference, candidate, verbose=True):
    """
    Comprehensive pseudocode comparison with BLEU score
    """
    # Tokenize
    # ref_tokens = reference.split()
    # cand_tokens = candidate.split()
    
    # # Calculate BLEU score
    # smoothing = SmoothingFunction().method7 # [TO DO]: figure out how to change dependencies to incorporate smoothing fucntion again
    # bleu_score = sentence_bleu([ref_tokens], cand_tokens, smoothing_function=smoothing)
    
    # if verbose:
    #     print("Reference:", reference)
    #     print("Candidate:", candidate)
    #     print(f"BLEU Score: {bleu_score:.4f}")
    #     print(f"Similarity: {bleu_score * 100:.1f}%")
        
    #     # Additional analysis
    #     ref_set = set(ref_tokens)
    #     cand_set = set(cand_tokens)
    #     common_tokens = ref_set.intersection(cand_set)
        
    #     print(f"\nCommon tokens: {common_tokens}")

    # return bleu_score
    bleu = sacrebleu.sentence_bleu(candidate, [reference])
    bleu_score = bleu.score / 100  # Convert to 0-1 scale
    
    if verbose:
        print("Reference:", reference)
        print("Candidate:", candidate)
        print(f"BLEU Score: {bleu_score:.4f}")
        print(f"Similarity: {bleu_score * 100:.1f}%")
        
        ref_tokens = reference.split()
        cand_tokens = candidate.split()
        ref_set = set(ref_tokens)
        cand_set = set(cand_tokens)
        common_tokens = ref_set.intersection(cand_set)
        
        print(f"\nCommon tokens: {common_tokens}")

    return bleu_score

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
        "avg_words_per_line": avg_words_per_line(pseudocode),
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

    averaged_metrics_dict = {key : value / problem_count for key, value in new_metrics_dict.items()}
    # print("average_metrics_dict: ", avgeraged_metrics_dict)

    return averaged_metrics_dict

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

def record_previous_best_solution(previous_best_path, prompt, dev_score, dev_feedback, it):
    previous_best = {"prompt": prompt, "response": prompt, "score": dev_score, "feedback": dev_feedback, "iter": it}
    with open(previous_best_path, "w") as file:
        json.dump(previous_best, file, indent=2)


def get_problem_readability_scores(problem_metrics, metric_key):
    # metric_keys = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "avg_word_length", "avg_score"]
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

def get_avg_test_case_length(problems_file_name):
    num_problems = 0
    num_total_test_cases = 0
    for problem in read_jsonl(problems_file_name):
        num_problems += 1
        input_output = problem["input_output"]
        num_test_cases = len(input_output)
        num_total_test_cases += num_test_cases
    return num_total_test_cases / num_problems if num_problems > 0 else 0
        # completion = problem["completion"]

def get_num_difficulty(problems_file_name, difficulty, start, end):
    num_problems = 0
    num_difficulty_problems = 0
    for problem in read_jsonl(problems_file_name):
        num_problems += 1
        problem_difficulty = problem["meta"]["difficulty"]
        if problem_difficulty == difficulty and num_problems >= start and num_problems < end :
            num_difficulty_problems +=1
    return num_difficulty_problems

def copy_difficulty_problems(problems_file_name, new_file_name, difficulty_map, limit):
    num_problems_map = {difficulty: 0 for difficulty in difficulty_map}
    result = []
    for problem in read_jsonl(problems_file_name):
        problem_difficulty = problem["meta"]["difficulty"]
        for difficulty in difficulty_map:
            if problem_difficulty == difficulty and num_problems_map[difficulty] < difficulty_map[difficulty] :
                num_problems_map[difficulty] += 1
                result.append(problem)
    write_jsonl(new_file_name, result)

def get_dataset_for_cosmetic_test(metrics_json_path_name, problems_dir, problems_filename, new_file_name, timestamp):
    '''
    Gets the pseudocodes from the given timestamp along with their scores for the test split of the autoencoder. 
    Only takes the last iteration and gets both positive and negative examples because we want to get both more 
    positive and negative examples through the cosmetic pipeline. 
    '''
    problems_file_name = os.path.join(problems_dir,problems_filename)
    problems = list_jsonl_task_ids(problems_file_name)
    num_problems = len(problems)

    pseudocode_examples = []

    positive_problems = set()
    negative_problems = set()

    with open(metrics_json_path_name, 'r') as file:
        pipeline_data = json.load(file)

    for i in range(len(pipeline_data)-1, len(pipeline_data)-2, -1 ): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
        # print('in for loop')
        entry = pipeline_data[i]
        for problem in read_jsonl(problems_file_name):
            task_id = problem["task_id"]
            prompt = problem["prompt"]
            entry_point = problem["entry_point"]
            if "leet_code" in problems_dir:
                test_cases = problem["input_output"]
            elif "human_eval" in problems_dir:
                test_cases = problem["test"]
            # else:
            #     test_cases = problem["test"]

            if "leet_code" in problems_dir:
                original_code = problem["prompt"] + problem["response"]
            elif "human_eval" in problems_dir:
                original_code = problem["prompt"] + problem["canonical_solution"]
            # else:
            #     original_code = problem["prompt"] + problem["canonical_solution"]

            score = entry[f"{task_id}_passing_rate"]

            iteration = entry["iter"]
            stage = entry["stage"]
            pseudocode_path_name = os.path.join(problems_dir, "outputs", timestamp, f"iter_{iteration}", "pseudocodes", f"{task_id}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()

            error_file_path = os.path.join(problems_dir, "outputs", timestamp, f"iter_{iteration}", "errors", f"{task_id}_errors.txt")
            if os.path.isfile(error_file_path):
                with open(error_file_path, 'r') as file:
                    error = file.read()
            else:
                error = ''
            if "leet_code" in problems_dir:
                pseudocode_examples.append({"task_id":task_id, "score": score, "pseudocode": pseudocode, "prompt": prompt, "entry_point": entry_point, "input_output": test_cases, "original_code": original_code, "error": error})
            elif "human_eval" in problems_dir:
                pseudocode_examples.append({"task_id":task_id, "score": score, "pseudocode": pseudocode, "prompt": prompt, "entry_point": entry_point, "test": test_cases, "original_code": original_code, "error": error})
            # else:
            #     pseudocode_examples.append({"task_id":task_id, "score": score, "pseudocode": pseudocode, "prompt": prompt, "entry_point": entry_point, "test": test_cases, "original_code": original_code, "error": error})
 
    # print("pseudocode examples:")
    # print(pseudocode_examples)
    write_jsonl(new_file_name, pseudocode_examples)
    
def get_dataset_for_cosmetic_train(metrics_json_path_name, problems_dir, problems_filename, new_file_name, timestamp):
    '''
    Gets the pseudocodes from the given timestamp along with their scores for the train split of the autoencoder. 
    Only takes positive examples to get more cosmetic changes through the cosmetic pipeline. 
    '''
    problems_file_name = os.path.join(problems_dir,problems_filename)
    problems = list_jsonl_task_ids(problems_file_name)
    num_problems = len(problems)

    true_positive_examples = []
    true_positive_problems = set()
    final_true_positive_examples = []

    with open(metrics_json_path_name, 'r') as file:
        pipeline_data = json.load(file)

    for i in range(len(pipeline_data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
        entry = pipeline_data[i]
        for problem in read_jsonl(problems_file_name):
            task_id = problem["task_id"]
            prompt = problem["prompt"]
            entry_point = problem["entry_point"]
            if "leet_code" in problems_dir:
                test_cases = problem["input_output"]
            elif "human_eval" in problems_dir:
                test_cases = problem["test"]

            # original_code = json_obj.get("prompt") + extract_code_blocks(json_obj.get("response"))[0]
            # response = problem["response"]
            # print('problem response:')
            # print(response)

            if "leet_code" in problems_dir:
                original_code = problem["prompt"] + problem["response"]
            elif "human_eval" in problems_dir:
                original_code = problem["prompt"] + problem["canonical_solution"]

            if entry[f"{task_id}_passing_rate"] == 1.0 and task_id not in true_positive_problems: # per set I only want one problem
                iteration = entry["iter"]
                stage = entry["stage"]
                pseudocode_path_name = os.path.join(problems_dir, "outputs", timestamp, f"iter_{iteration}", "pseudocodes", f"{task_id}_pseudocode_{stage}.txt")
            # pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_pseudocode_{stage}.txt")

                with open(pseudocode_path_name, 'r') as file:
                    pseudocode = file.read()
                if "leet_code" in problems_dir:
                    true_positive_examples.append({"task_id":task_id, "score": 1.0, "pseudocode": pseudocode, "prompt": prompt, "entry_point": entry_point, "input_output": test_cases, "original_code": original_code})
                elif "human_eval" in problems_dir:
                    true_positive_examples.append({"task_id":task_id, "score": 1.0, "pseudocode": pseudocode, "prompt": prompt, "entry_point": entry_point, "test": test_cases, "original_code": original_code})
                true_positive_problems.add(task_id)
    
        if len(true_positive_problems) == num_problems:
            break

    write_jsonl(new_file_name, true_positive_examples)

    return true_positive_examples

def get_cosmetic_dataset(cfg):
    # GET PSEUDOCODES FROM THE AUTOENCODER PIPELINE FOR TRAIN OR TEST SPLIT
    # autoencoder_timestamp = '2025-09-18_21-00-18'
    autoencoder_metrics_file = os.path.join(ROOT_DIR, "data", "autoencoder", cfg.dataset, "metrics", f"{cfg.autoencoder_timestamp}_metrics.json")
    autoencoder_dir = f"{ROOT_DIR}/data/autoencoder/{cfg.dataset}"
    if cfg.dataset == 'leet_code':
        autoencoder_problems_filename = f'LeetCodeDataset-{cfg.autoencoder_version}-{cfg.split}.jsonl'
    elif cfg.dataset == 'human_eval':
        autoencoder_problems_filename = f'HumanEval-{cfg.split}.jsonl'
    
    new_file_name = os.path.join(ROOT_DIR, "data", "cosmetic", cfg.dataset, f"AutoEncoderPseudocodes_{cfg.cosmetic_version}-{cfg.split}.jsonl")
    
    if cfg.split == 'train':
        positive_examples = get_dataset_for_cosmetic_train(autoencoder_metrics_file, autoencoder_dir, autoencoder_problems_filename, new_file_name, cfg.autoencoder_timestamp)
    elif cfg.split == 'test':
        pseudocode_examples = get_dataset_for_cosmetic_test(autoencoder_metrics_file, autoencoder_dir, autoencoder_problems_filename, new_file_name, cfg.autoencoder_timestamp)

def get_classifier_dataset(cfg, limit=150):
    '''
    Combines the pseudocodes from the autoencoder pipeline and the cosmetic pipeline to create a final dataset of pseudocodes
    for the classifier.

    limit is the max number of pseudocodes in the test split dataset
    '''
    # autoencoder_timestamp = '2025-09-18_21-00-18' # leet_code
    # autoencoder_timestamp = '2025-09-24_15-05-02' #human_eval
    autoencoder_metrics_file = os.path.join(ROOT_DIR, "data", "autoencoder", cfg.dataset, "metrics", f"{cfg.autoencoder_timestamp}_metrics.json")

    # cosmetic_timestamp = '2025-09-29_13-46-17'
    cosmetic_metrics_file = os.path.join(ROOT_DIR, "data", "cosmetic", cfg.dataset, "metrics", f"{cfg.cosmetic_timestamp}_metrics.json")
    
    dataset_file_name = ''
    if cfg.dataset == 'leet_code':
        autoencoder_problems_filename = f'LeetCodeDataset-{cfg.autoencoder_version}-{cfg.split}.jsonl'
        dataset_file_name = 'LeetCode'
    elif cfg.dataset == 'human_eval':
        autoencoder_problems_filename = f'HumanEval-{cfg.split}.jsonl'
        dataset_file_name = 'HumanEval'

    autoencoder_dir = f"{ROOT_DIR}/data/autoencoder/{cfg.dataset}"
    
    cosmetic_dir = f"{ROOT_DIR}/data/cosmetic/{cfg.dataset}"
    cosmetic_problems_filename = f"AutoEncoderPseudocodes_{cfg.autoencoder_timestamp}.jsonl"

    #########################
    if cfg.split == 'train':
        problem_results, dev_set_results = get_dataset_for_classifier_train(autoencoder_metrics_file, cosmetic_metrics_file, autoencoder_dir, cosmetic_dir, autoencoder_problems_filename, cosmetic_problems_filename, cfg.autoencoder_timestamp, cfg.cosmetic_timestamp, iterations, limit)
        
        train_set_filename = os.path.join(ROOT_DIR, "data", "classifier", cfg.dataset, f"{dataset_file_name}Pseudocodes-v0.{cfg.classifier_version}.0-train.jsonl" )
        dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier", cfg.dataset, f"{dataset_file_name}Pseudocodes-v0.{cfg.classifier_version}.0-dev.jsonl")
        
        write_dataset_to_file(problem_results, train_set_filename)
        write_dataset_to_file(dev_set_results, dev_set_filename)

    elif cfg.split == 'test':    
        problem_results = get_dataset_for_classifier_test(cosmetic_metrics_file, cosmetic_dir, cosmetic_problems_filename, cfg.cosmetic_timestamp, limit)
        test_set_filename = os.path.join(ROOT_DIR, "data", "classifier", cfg.dataset, f"{dataset_file_name}Pseudocodes-v0.{cfg.classifier_version}.0-test.jsonl" )
        write_dataset_to_file(problem_results, test_set_filename)

    

def write_dataset_to_file(true_positive_examples, positive_examples_file_name):
    write_jsonl(positive_examples_file_name, true_positive_examples)

def write_errors_to_file(error_file_path, errors, num_errors):
    for task_id in errors:
        error_list = errors[task_id]
        problem_error_file_path = os.path.join(error_file_path, f"{task_id}_errors.txt")
        if error_list:
            with open(problem_error_file_path, 'w') as file:
                file.write(str(error_list[:num_errors]))
    # for entry in errors:
    #     task_id = entry["task_id"]
    #     error_list = entry["error_list"]
    #     problem_error_file_path = os.path.join(error_file_path, f"{task_id}_errors.txt")
    #     if error_list:
    #         with open(problem_error_file_path, 'w') as file:
    #             file.write(str(error_list[:num_errors]))
def get_dataset_for_classifier_test(cosmetic_metrics_file, cosmetic_dir, cosmetic_problems_filename, cosmetic_timestamp, limit):
    problems = list_jsonl_task_ids(os.path.join(cosmetic_dir, cosmetic_problems_filename)) 
    
    true_positive_problems = set()
    true_negative_problems = set()
    
    true_positive_examples = {problem : [] for problem in problems}
    true_negative_examples = {problem : [] for problem in problems}

    problem_positive_count_dict = {problem: 0 for problem in problems}
    problem_negatives_count_dict = {problem: 0 for problem in problems}
    
       
    with open(cosmetic_metrics_file, 'r') as file:
        cosmetic_pipeline_data = json.load(file)

    # for i in range(len(first_pipeline_data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
    for i in range(0, 6, 1):    
        entry = cosmetic_pipeline_data[i]
        current_iter = entry["iter"]
        print('current iter:')
        print(current_iter)
        for problem in problems:
            if entry[f"{problem}_passing_rate"] == 1.0: # per set I only want one problem
                true_positive_examples[problem].append({"score": 1.0, "iter": entry["iter"], "stage": entry["stage"]})
                true_positive_problems.add(problem)
                problem_positive_count_dict[problem] += 1
            else:
                true_negative_examples[problem].append({"score": entry[f"{problem}_passing_rate"], "iter": entry["iter"], "stage": entry["stage"]})
                true_negative_problems.add(problem)
                problem_negatives_count_dict[problem] += 1

    print('len of positive problems:', len(true_positive_problems))
    print('len of negative problems: ', len(true_negative_problems))

    problems_overlap = true_positive_problems.intersection(true_negative_problems)
    limited_problems = random.sample(sorted(problems_overlap), min(len(problems_overlap), limit))
    print('size of overlap: ', len(limited_problems))

    problems_json_file = os.path.join(cosmetic_dir,cosmetic_problems_filename)

    problem_results = []

    for entry in read_jsonl(problems_json_file):
        problem = entry["task_id"]
        
        if problem in limited_problems:
            if "leet_code" in cosmetic_dir:
                original_code = entry["prompt"] + entry["response"]
            elif "human_eval" in cosmetic_dir:
                original_code = entry["prompt"] + entry["canonical_solution"]
            elif 'pseudocode_labels' in cosmetic_problems_filename:
                original_code = entry["original_code"]

            prompt = entry["prompt"]
            entry_point = entry["entry_point"]
            if "leet_code" in cosmetic_dir:
                test_cases = entry["input_output"]
                test_cases_key = 'input_output'
            elif "human_eval" in cosmetic_dir:
                test_cases = entry["test"]
                test_cases_key = 'test'
            else:
                test_cases = entry["test"]
                test_cases_key = 'test'
            train_set = []
            true_positive_entries = true_positive_examples[problem]
            true_negative_entries = true_negative_examples[problem]

            # get true positive example
            iteration = true_positive_entries[0]["iter"]
            score = true_positive_entries[0]["score"]
            stage = true_positive_entries[0]["stage"]
            pseudocode_path_name = os.path.join(cosmetic_dir, "outputs", cosmetic_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            true_positive_pseudocode = pseudocode
            train_set.append({"label": "true_positive","pseudocode": pseudocode,  "score": score})

            # get true negative example
            iteration = true_negative_entries[0]["iter"]
            score = true_negative_entries[0]["score"]
            stage = true_negative_entries[0]["stage"]
            pseudocode_path_name = os.path.join(cosmetic_dir, "outputs", cosmetic_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            error_file_path = os.path.join(cosmetic_dir, "outputs", first_timestamp, f"iter_{iteration}", "errors", f"{problem}_errors.txt")
            if os.path.isfile(error_file_path):
                with open(error_file_path, 'r') as file:
                    error = file.read()
            else:
                error = ''
            train_set.append({"label": "true_negative","pseudocode": pseudocode,  "score": score, "error": error, "true_positive": true_positive_pseudocode})

            problem_results.append({"task_id": problem, "pseudocode_dataset": train_set, "original_code": original_code, "prompt": prompt, "entry_point": entry_point, f"{test_cases_key}": test_cases})
    return problem_results
            

def get_dataset_for_classifier_train(autoencoder_metrics_file, cosmetic_metrics_file, first_problems_dir, second_problems_dir, first_problems_filename, second_problems_filename, first_timestamp, second_timestamp, num_iterations, limit):
    # First step: go into the metrics json file and see which iters have a score of 1.0 and which don't.
    # so in the pandas dataframe we have the following columns: problem, pseudocode, score
    # i guess that begs the other question of how many examples to have per problem? i guess just one for now.
    # problems_dir_path = Path(problems_dir)
    # problems = {problem.name for problem in problems_dir_path.iterdir() if problem.is_dir() and problem.name != 'metrics'}
    # problems = list_jsonl_task_ids(os.path.join(problems_dir, dir_file_name))
    # problems = list_jsonl_task_ids(os.path.join(first_problems_dir,first_problems_filename))

    # Use the second problems_file_name because the second filters from problems from the first:
    problems = list_jsonl_task_ids(os.path.join(second_problems_dir,second_problems_filename))
    num_problems = len(problems)
    
    true_positive_problems = set()
    true_negative_problems = set()
    near_miss_problems = set()
    cosmetic_problems = set()
    true_positive_examples = {problem : [] for problem in problems}
    true_negative_examples = {problem : [] for problem in problems}
    near_miss_examples = {problem : [] for problem in problems}
    cosmetic_examples = {problem : [] for problem in problems}

    with open(autoencoder_metrics_file, 'r') as file:
        autoencoder_pipeline_data = json.load(file)

    #load in the data for the second pipeline
    with open(cosmetic_metrics_file, 'r') as file:
        cosmetic_pipeline_data = json.load(file)


    # Now 'data' is a Python list containing your dictionary
    # print(data)

    dataset_list = []

    # Second step: get the iters and rounds of the pseudocodes, now we gotta go find the pseudocodes
    # [TO DO]: not sure if this is the best approach to get the scores of the problems... i think i can do what HumanEval does and read a jsonl file? not sure what's easiest. honeslty this is fine.
    # this is for the true positives, true negatives, near misses

    # The following dictionaries keep track of how many iters fall under this bucket.
    problem_positive_count_dict = {problem: 0 for problem in problems}
    problem_negatives_count_dict = {problem: 0 for problem in problems}
    problem_near_miss_count_dict = {problem: 0 for problem in problems}
    problem_near_pass_count_dict = {problem: 0 for problem in problems}

    near_miss_threshold = 0.8

    # for i in range(len(first_pipeline_data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
    #     entry = first_pipeline_data[i]
    #     for problem in problems:
    #         if entry[f"{problem}_passing_rate"] == 1.0 and problem not in true_positive_problems: # per set I only want one problem
    #             true_positive_examples.append({"problem":problem, "score": 1.0, "iter": entry["iter"], "stage": entry["stage"]})
    #             true_positive_problems.add(problem)
    #         elif entry[f"{problem}_passing_rate"] < near_miss_threshold and problem not in true_negative_problems:
    #             true_negative_examples.append({"problem":problem, "score": 0, "iter": entry["iter"], "stage": entry["stage"]})
    #             true_negative_problems.add(problem)
    #         elif entry[f"{problem}_passing_rate"] >= near_miss_threshold and entry[f"{problem}_passing_rate"] < 1.0 and problem not in true_negative_problems:
    #             near_miss_examples.append({"problem":problem, "score": 0, "iter": entry["iter"], "stage": entry["stage"]})
    #             near_miss_problems.add(problem)
    #     if len(true_positive_problems) == num_problems and len(true_negative_problems) == num_problems and len(near_pass_problems) == num_problems: # sets are maxed out
    #         break
    for i in range(len(autoencoder_pipeline_data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
        entry = autoencoder_pipeline_data[i]
        for problem in problems:
            if entry[f"{problem}_passing_rate"] == 1.0: # per set I only want one problem
                true_positive_examples[problem].append({"score": 1.0, "iter": entry["iter"], "stage": entry["stage"]})
                true_positive_problems.add(problem)
                problem_positive_count_dict[problem] += 1
            elif entry[f"{problem}_passing_rate"] < near_miss_threshold:
                true_negative_examples[problem].append({"score": 0, "iter": entry["iter"], "stage": entry["stage"]})
                true_negative_problems.add(problem)
                problem_negatives_count_dict[problem] += 1
            elif entry[f"{problem}_passing_rate"] >= near_miss_threshold and entry[f"{problem}_passing_rate"] < 1.0:
                near_miss_examples[problem].append({"score": entry[f"{problem}_passing_rate"], "iter": entry["iter"], "stage": entry["stage"], "pipeline": "first"})
                near_miss_problems.add(problem)
                problem_near_miss_count_dict[problem] += 1

    bleu_score_threshold = 0.2
    for i in range(len(cosmetic_pipeline_data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
        entry = cosmetic_pipeline_data[i]
        for problem in problems:
            if entry[f"{problem}_passing_rate"] == 1.0 and (autoencoder_pipeline_json_path_name != cosmetic_pipeline_metrics_path) and entry[f"{problem}_bleu_score"] < bleu_score_threshold :
                cosmetic_examples[problem].append({"score": 1.0, "iter": entry["iter"], "stage": entry["stage"]})
                cosmetic_problems.add(problem)
                problem_near_pass_count_dict[problem] += 1
            elif entry[f"{problem}_passing_rate"] >= near_miss_threshold and entry[f"{problem}_passing_rate"] < 1.0 and (autoencoder_metrics_file != cosmetic_metrics_file):
                near_miss_examples[problem].append({"score": entry[f"{problem}_passing_rate"], "iter": entry["iter"], "stage": entry["stage"], "pipeline": "second"})
                near_miss_problems.add(problem)
                problem_near_miss_count_dict[problem] += 1

    # Now we will calculate how many problems in each bucket pass the threshold for how many examples they hold
    minimum_problem_iter_count = 1
    # num_positives_count = 0
    # num_negatives_count = 0
    # num_near_miss_count = 0
    # num_near_pass_count = 0
    positive_iter_count_problems = set()
    negative_iter_count_problems = set()
    near_miss_iter_count_problems = set()
    cosmetic_iter_count_problems = set()

    # for problem in problems:
    #     if problem_positive_count_dict[problem] >= minimum_problem_iter_count:
    #         num_positives_count += 1
    #         positive_iter_count_problems.add(problem)
    #     if problem_negatives_count_dict[problem] >= minimum_problem_iter_count:
    #         num_negatives_count += 1
    #         negative_iter_count_problems.add(problem)
    #     if problem_near_miss_count_dict[problem] >= minimum_problem_iter_count:
    #         num_near_miss_count += 1
    #         near_miss_iter_count_problems.add(problem)
    #     if problem_near_pass_count_dict[problem] >= minimum_problem_iter_count:
    #         num_near_pass_count += 1
    #         cosmetic_iter_count_problems.add(problem)
    for problem in problems:
        if len(true_positive_examples[problem]) >= minimum_problem_iter_count:
            positive_iter_count_problems.add(problem)
        if len(true_negative_examples[problem]) >= minimum_problem_iter_count:
            negative_iter_count_problems.add(problem)
        if len(near_miss_examples[problem]) >= minimum_problem_iter_count:
            near_miss_iter_count_problems.add(problem)
        if len(cosmetic_examples[problem]) >= minimum_problem_iter_count:
            cosmetic_iter_count_problems.add(problem)

    intersection_one_version = positive_iter_count_problems.intersection(negative_iter_count_problems, near_miss_iter_count_problems, cosmetic_iter_count_problems)

    print(f'num of problems that have at least {minimum_problem_iter_count} for the true positive bucket: ', len(positive_iter_count_problems))
    print(f'num of problems that have at least {minimum_problem_iter_count} for the true negative bucket: ', len(negative_iter_count_problems))
    print(f'num of problems that have at least {minimum_problem_iter_count} for the near miss bucket: ', len(near_miss_iter_count_problems))
    print(f'num of problems that have at least {minimum_problem_iter_count} for the near pass bucket: ', len(cosmetic_iter_count_problems))
    print(f'len of problems that overlap for at least {minimum_problem_iter_count} versions for the problems is: ', len(intersection_one_version))


    minimum_problem_iter_count = 2
    positive_iter_count_problems = set()
    negative_iter_count_problems = set()
    near_miss_iter_count_problems = set()
    cosmetic_iter_count_problems = set()
    
    for problem in problems:
        if len(true_positive_examples[problem]) >= minimum_problem_iter_count:
            positive_iter_count_problems.add(problem)
        if len(true_negative_examples[problem]) >= minimum_problem_iter_count:
            negative_iter_count_problems.add(problem)
        if len(near_miss_examples[problem]) >= minimum_problem_iter_count:
            near_miss_iter_count_problems.add(problem)
        if len(cosmetic_examples[problem]) >= minimum_problem_iter_count:
            cosmetic_iter_count_problems.add(problem)

    intersection_two_versions = positive_iter_count_problems.intersection(negative_iter_count_problems, near_miss_iter_count_problems, cosmetic_iter_count_problems)

    one_and_two_versions = intersection_two_versions.intersection(intersection_one_version)
    print(f'num of problems that have at least {minimum_problem_iter_count} for the true positive bucket: ', len(positive_iter_count_problems))
    print(f'num of problems that have at least {minimum_problem_iter_count} for the true negative bucket: ', len(negative_iter_count_problems))
    print(f'num of problems that have at least {minimum_problem_iter_count} for the near miss bucket: ', len(near_miss_iter_count_problems))
    print(f'num of problems that have at least {minimum_problem_iter_count} for the near pass bucket: ', len(cosmetic_iter_count_problems))
    print(f'len of problems that overlap for at least {minimum_problem_iter_count} versions for the problems is: ', len(intersection_two_versions))

    print(f'len of problems that overlap for the one and two versions for the problems is: ', len(one_and_two_versions))

    remaining_problems = intersection_one_version - one_and_two_versions 
    print('len of remaining_problems:', len(remaining_problems))
    rest_of_problems = random.sample(sorted(remaining_problems), min(limit - len(one_and_two_versions), len(remaining_problems)))
    print('len of rest_of_problems: ', len(rest_of_problems))
    final_set_problems = set(rest_of_problems) | one_and_two_versions
    print('len of final_set_problems: ', len(final_set_problems))

    # near_pass_examples = []
    # near_pass_problems = set()
    # for example in passed_at_least_once_examples:
    #     problem_failure_count = problem_failure_count_dict[example["problem"]]
    #     if problem_failure_count >= num_iter_to_fail:
    #         near_pass_examples.append(example)
    #         near_pass_problems.add(example["problem"])

    # Step 3: Make the buckets as evenly sized as possible
    print("BEFORE creating disjoint sets:")
    print("len of true positive problems: ", len(true_positive_problems))
    print("len of true negative problems: ", len(true_negative_problems))
    print("len of near misses problems: ", len(near_miss_problems))


    #what the structure should look like:
    # {"problem":problem, "pseudocode_dataset": [{"label": "true_positive","pseudocode": pseudocode,  "score":}, {"label": "true_negative","pseudocode": pseudocode,  "score":}]}
    # Get pseudocodes for intersection:
    problem_results = []
    dev_set_results = []
    # for problem in intersection_one_version:
    # Use the second problems_file_name because the second filters from problems from the first:
    problems_json_file = os.path.join(second_problems_dir,second_problems_filename)
    
    # for problem in final_set_problems:
    for entry in read_jsonl(problems_json_file):
        problem = entry["task_id"]
        
        if problem in final_set_problems:
            original_code = entry["original_code"]
            prompt = entry["prompt"]
            entry_point = entry["entry_point"]
            if "leet_code" in first_problems_dir:
                test_cases = entry["input_output"]
                test_cases_key = 'input_output'
            elif "human_eval" in first_problems_dir:
                test_cases = entry["test"]
                test_cases_key = 'test'
            buckets_4_train = []
            buckets_4_dev = []
            true_positive_entries = true_positive_examples[problem]
            true_negative_entries = true_negative_examples[problem]
            near_miss_entries = near_miss_examples[problem]
            cosmetic_entries = cosmetic_examples[problem]

            # get true positive example
            iteration = true_positive_entries[0]["iter"]
            score = true_positive_entries[0]["score"]
            stage = true_positive_entries[0]["stage"]
            pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            true_positive_pseudocode = pseudocode
            buckets_4_train.append({"label": "true_positive","pseudocode": pseudocode,  "score": score})

            # get true negative example
            iteration = true_negative_entries[0]["iter"]
            score = true_negative_entries[0]["score"]
            stage = true_negative_entries[0]["stage"]
            pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            error_file_path = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iteration}", "errors", f"{problem}_errors.txt")
            if os.path.isfile(error_file_path):
                with open(error_file_path, 'r') as file:
                    error = file.read()
            else:
                error = ''
            buckets_4_train.append({"label": "true_negative","pseudocode": pseudocode,  "score": score, "error": error, "true_positive":true_positive_pseudocode})

            # get near_miss example
            iteration = near_miss_entries[0]["iter"]
            score = near_miss_entries[0]["score"]
            stage = near_miss_entries[0]["stage"]
            pipeline = near_miss_entries[0]["pipeline"]
            # This is because near_miss comes from both the first and second pipelines
            if pipeline == "first":
                problems_dir_name = first_problems_dir
                problem_timestamp = first_timestamp
            else:
                problems_dir_name = second_problems_dir
                problem_timestamp = second_timestamp
            pseudocode_path_name = os.path.join(problems_dir_name, "outputs", problem_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            error_file_path = os.path.join(problems_dir_name, "outputs", first_timestamp, f"iter_{iteration}", "errors", f"{problem}_errors.txt")
            if os.path.isfile(error_file_path):
                with open(error_file_path, 'r') as file:
                    error = file.read()
            else:
                error = ''
            buckets_4_train.append({"label": "near_miss","pseudocode": pseudocode,  "score": score, "error": error, "true_positive":true_positive_pseudocode})

            # get cosmetic example
            iteration = cosmetic_entries[0]["iter"]
            score = cosmetic_entries[0]["score"]
            stage = cosmetic_entries[0]["stage"]
            pseudocode_path_name = os.path.join(second_problems_dir, "outputs", second_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            buckets_4_train.append({"label": "cosmetic","pseudocode": pseudocode,  "score": score, "true_positive": true_positive_pseudocode})

            problem_results.append({"task_id":problem, "pseudocode_dataset": buckets_4_train, "original_code": original_code, "prompt": prompt, "entry_point": entry_point, f"{test_cases_key}": test_cases})

            # Get dev set:
            if problem in intersection_two_versions:
                if len(true_positive_entries) > 1:
                    iteration = true_positive_entries[1]["iter"]
                    score = true_positive_entries[1]["score"]
                    stage = true_positive_entries[1]["stage"]
                    pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
                    with open(pseudocode_path_name, 'r') as file:
                        pseudocode = file.read()
                    true_positive_pseudocode = pseudocode
                    buckets_4_dev.append({"label": "true_positive","pseudocode": pseudocode,  "score": score})

                if len(true_negative_entries) > 1:
                    iteration = true_negative_entries[1]["iter"]
                    score = true_negative_entries[1]["score"]
                    stage = true_negative_entries[1]["stage"]
                    pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
                    with open(pseudocode_path_name, 'r') as file:
                        pseudocode = file.read()
                    error_file_path = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iteration}", "errors", f"{problem}_errors.txt")
                    if os.path.isfile(error_file_path):
                        with open(error_file_path, 'r') as file:
                            error = file.read()
                    else:
                        error = ''
                    buckets_4_dev.append({"label": "true_negative","pseudocode": pseudocode,  "score": score, "error": error, "true_positive":true_positive_pseudocode})

                if len(near_miss_entries) > 1:
                    iteration = near_miss_entries[1]["iter"]
                    score = near_miss_entries[1]["score"]
                    stage = near_miss_entries[1]["stage"]
                    pipeline = near_miss_entries[1]["pipeline"]
                    # This is because near_miss comes from both the first and second pipelines
                    if pipeline == "first":
                        problems_dir_name = first_problems_dir
                        problem_timestamp = first_timestamp
                    else:
                        problems_dir_name = second_problems_dir
                        problem_timestamp = second_timestamp
                    pseudocode_path_name = os.path.join(problems_dir_name, "outputs", problem_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
                    with open(pseudocode_path_name, 'r') as file:
                        pseudocode = file.read()
                    error_file_path = os.path.join(problems_dir_name, "outputs", first_timestamp, f"iter_{iteration}", "errors", f"{problem}_errors.txt")
                    if os.path.isfile(error_file_path):
                        with open(error_file_path, 'r') as file:
                            error = file.read()
                    else:
                        error = ''
                    buckets_4_dev.append({"label": "near_miss","pseudocode": pseudocode,  "score": score, "error": error, "true_positive":true_positive_pseudocode})

                if len(cosmetic_entries) > 1:
                    iteration = cosmetic_entries[1]["iter"]
                    score = cosmetic_entries[1]["score"]
                    stage = cosmetic_entries[1]["stage"]
                    pseudocode_path_name = os.path.join(second_problems_dir, "outputs", second_timestamp, f"iter_{iteration}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
                    with open(pseudocode_path_name, 'r') as file:
                        pseudocode = file.read()
                    buckets_4_dev.append({"label": "cosmetic","pseudocode": pseudocode,  "score": score, "true_positive": true_positive_pseudocode})

                dev_set_results.append({"task_id":problem, "pseudocode_dataset": buckets_4_dev, "original_code": original_code, "prompt": prompt, "entry_point": entry_point, f"{test_cases_key}": test_cases})

    return problem_results, dev_set_results

    # Step 4: find the pseudocodes
    # [TO DO]: hmmm this is maybe better done with a jsonl format
    final_true_positive_examples = []
    final_true_negative_examples = []
    final_near_miss_examples = []
    final_near_pass_examples = []
    for entry in true_positive_examples:
        problem = entry["problem"]
        iter = entry["iter"]
        score = entry["score"]
        stage = entry["stage"]

        if problem in intersection_result:
            pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iter}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            # pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_pseudocode_{stage}.txt")

            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            
            final_true_positive_examples.append({"problem":problem, "score": score, "pseudocode": pseudocode})

    for entry in true_negative_examples:
        # print('entry:')
        # print(entry)
        problem = entry["problem"]
        iter = entry["iter"]
        score = entry["score"]
        stage = entry["stage"]

        # [TO DO]: change pseudocode_path_name
        # if problem in final_true_negative_problems:
        if problem in intersection_result:
            pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iter}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            # pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_pseudocode_{stage}.txt")

            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            
            final_true_negative_examples.append({"problem":problem, "score": score, "pseudocode": pseudocode})

    for entry in near_miss_examples:
        # print('entry:')
        # print(entry)
        problem = entry["problem"]
        iter = entry["iter"]
        score = entry["score"]
        stage = entry["stage"]

        # [TO DO]: change pseudocode_path_name
        # if problem in final_near_miss_problems:
        if problem in intersection_result:
            pseudocode_path_name = os.path.join(first_problems_dir, "outputs", first_timestamp, f"iter_{iter}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            # pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_pseudocode_{stage}.txt")

            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            
            final_near_miss_examples.append({"problem":problem, "score": score, "pseudocode": pseudocode})

    # for entry in near_miss_examples:
    for entry in cosmetic_examples:
        # print('entry:')
        # print(entry)
        problem = entry["problem"]
        iter = entry["iter"]
        score = entry["score"]
        stage = entry["stage"]

        # [TO DO]: change pseudocode_path_name
        # if problem in final_near_pass_problems:
        if problem in intersection_result:
            pseudocode_path_name = os.path.join(second_problems_dir, "outputs", second_timestamp, f"iter_{iter}", "pseudocodes", f"{problem}_pseudocode_{stage}.txt")
            # pseudocode_path_name = os.path.join(problems_dir, problem, "outputs", "pseudocodes", timestamp, f"iter_{iter}_pseudocode_{stage}.txt")

            with open(pseudocode_path_name, 'r') as file:
                pseudocode = file.read()
            
            final_near_pass_examples.append({"problem":problem, "score": score, "pseudocode": pseudocode})

    # what do i want the final jsonl file to look like:
    # {"problem":problem, "pseudocode_dataset": [{"label": "true_positive","pseudocode": pseudocode,  "score":}, {"label": "true_negative","pseudocode": pseudocode,  "score":}]}
    # this is what the input_output list looks like 
    # "input_output": [{"input": "s = \"abcabcbb\"", "output": "3"}, {"input": "s = \"bbbbb\"", "output": "1"}, {"input": "s = \"pwwkew\"", "output": "3"}, {"input": "s = \"abcdabcabcabcd\"", "output": "4"}, {"input": "s = \"abcdefgabcdefgabcdefgabcdefg\"", "output": "7"}, {"input": "s = \"aabbccddeeff\"", "output": "2"}, {"input": "s = \"sldfjldskfjdslkfjsdkljflkjsdfljfsdlkflskdjflsdjflskdjflsdkjflsdfjlsd\"", "output": "6"}, {"input": "s = \"racecar\"", "output": "4"}, {"input": "s = \"abcdefghijklmnopqrstuvwxyz\"", "output": "26"}, {"input": "s = \"aabacbebebe\"", "output": "4"}, {"input": "s = \"ekdvdfis\"", "output": "5"}, {"input": "s = \"aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890abcdefghijklmnopqrstuvwxyz\"", "output": "36"}, {"input": "s = \"abbaabbaabba\"", "output": "2"}, {"input": "s = \"aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz\"", "output": "2"}, {"input": "s = \"abcdefghihgfedcba\"", "output": "9"}, {"input": "s = \"abcdeffedcba\"", "output": "6"}, {"input": "s = \"aaaaaaaabbbbbbbccccccdddddeeeeeeffffffffggggggg\"", "output": "2"}, {"input": "s = \"tmmzuxt\"", "output": "5"}, {"input": "s = \"nfpdmpi\"", "output": "5"}, {"input": "s = \"anviaj\"", "output": "5"}, {"input": "s = \"abcdeabcde\"", "output": "5"}, {"input": "s = \"abcdabcabcd\"", "output": "4"}, {"input": "s = \"dvdf\"", "output": "3"}, {"input": "s = \"zyxwvutsrqponmlkjihgfedcba\"", "output": "26"}, {"input": "s = \"abcdabcdeabcdabcdeabcd\"", "output": "5"}, {"input": "s = \"rjqzupkoz\"", "output": "8"}, {"input": "s = \"ababababababababab\"", "output": "2"}, {"input": "s = \"!@#$%^&*()_+!@#$%^&*()_+\"", "output": "12"}, {"input": "s = \"cdddddddddddddd\"", "output": "2"}, {"input": "s = \"wobgrovw\"", "output": "6"}, {"input": "s = \"abba\"", "output": "2"}, {"input": "s = \"abcbacabc\"", "output": "3"}, {"input": "s = \"ohvhjdml\"", "output": "6"}, {"input": "s = \"123456789012345678901234567890\"", "output": "10"}, {"input": "s = \"aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz1234567890!@#$%^&*()_+\"", "output": "23"}, {"input": "s = \"12345678901234567890\"", "output": "10"}]


    # print('length of positive examples: ', len(final_true_positive_examples))
    # print('length of negative examples: ', len(final_true_negative_examples))
    # print('length of negative examples: ', len(final_near_miss_examples))
    # print('length of negative examples: ', len(final_near_pass_examples))
    
    # return final_true_positive_examples, final_true_negative_examples, final_near_miss_examples, final_near_pass_examples

def create_disjoint_sets_4(set_a, set_b, set_c, set_d):
    """
    Attempts to create four disjoint sets of equal size from the input sets.
    Returns the largest possible disjoint sets of equal size.
    """
    # Target size is the minimum original set size
    target_size = min(len(set_a), len(set_b), len(set_c), len(set_d))
    
    # Phase 1: Identify problems unique to each set (safe to include)
    all_sets = set_a | set_b | set_c | set_d
    other_sets = set_b | set_c | set_d
    only_a = set_a - other_sets
    
    other_sets = set_a | set_c | set_d
    only_b = set_b - other_sets
    
    other_sets = set_a | set_b | set_d
    only_c = set_c - other_sets
    
    other_sets = set_a | set_b | set_c
    only_d = set_d - other_sets
    
    # Identify problems that appear in multiple sets
    conflict_set = (set_a & set_b) | (set_a & set_c) | (set_a & set_d) | \
                   (set_b & set_c) | (set_b & set_d) | \
                   (set_c & set_d)
    
    new_a, new_b, new_c, new_d = set(), set(), set(), set()
    
    # Add all unique problems 
    for problem in only_a:
        if len(new_a) < target_size:
            new_a.add(problem)
    
    for problem in only_b:
        if len(new_b) < target_size:
            new_b.add(problem)
            
    for problem in only_c:
        if len(new_c) < target_size:
            new_c.add(problem)
            
    for problem in only_d:
        if len(new_d) < target_size:
            new_d.add(problem)
    
    # Now, strategically assign conflicting problems
    for problem in conflict_set:
        # Check which sets this problem belongs to
        in_a = problem in set_a
        in_b = problem in set_b
        in_c = problem in set_c
        in_d = problem in set_d
        
        # Count how many sets still need this problem
        sets_that_need_it = []
        if in_a and len(new_a) < target_size:
            sets_that_need_it.append('a')
        if in_b and len(new_b) < target_size:
            sets_that_need_it.append('b')
        if in_c and len(new_c) < target_size:
            sets_that_need_it.append('c')
        if in_d and len(new_d) < target_size:
            sets_that_need_it.append('d')
        
        # If only one set can take it, assign it there
        if len(sets_that_need_it) == 1:
            if sets_that_need_it[0] == 'a':
                new_a.add(problem)
            elif sets_that_need_it[0] == 'b':
                new_b.add(problem)
            elif sets_that_need_it[0] == 'c':
                new_c.add(problem)
            else:
                new_d.add(problem)
        
        # If multiple sets can take it, use a strategy...
        elif len(sets_that_need_it) > 1:
            # Strategy: Assign to the set that has the fewest options left
            options_count = {
                'a': len(set_a - new_a - new_b - new_c - new_d),
                'b': len(set_b - new_a - new_b - new_c - new_d),
                'c': len(set_c - new_a - new_b - new_c - new_d),
                'd': len(set_d - new_a - new_b - new_c - new_d)
            }
            
            # Assign to the set with the least remaining options
            chosen_set = min(sets_that_need_it, key=lambda x: options_count[x])
            if chosen_set == 'a':
                new_a.add(problem)
            elif chosen_set == 'b':
                new_b.add(problem)
            elif chosen_set == 'c':
                new_c.add(problem)
            else:
                new_d.add(problem)
    
    return new_a, new_b, new_c, new_d


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

        # print('output_responses: ', output_responses)

        # Write codes to file:
        output_list = []
        for entry in output_responses:
            try:
                new_entry = int(entry.strip('\n`*'))
                output_list.append(new_entry)
            except:
                output_list.append(-1)
        # output_list = [int(entry.strip('\n`*')) for entry in output_responses]
        # for idx in range(len(output_responses)):
        #     decoding = output_responses[idx]
        #     code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
        #     code = textwrap.dedent(code_blocks[0])
        #     result = int(code)
        #     output_list.append(result)
        # print('output_list: ', output_list)
        print('len of output list: ', len(output_list))

        return output_list

def gen_multi_chat_decodings(dataset_name, problem_cases, decoding_prompt, pseudocode_encoding_list, stage, timestamp, it, client):
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

    # Write codes to file:
    code_file_path_list = []
    task_pseudocodes_codes = {}
    code_decodings_list = []
    # for idx, problem_file_path in enumerate(problem_file_path_list):
    for idx, problem in enumerate(problem_cases):
        decoding = code_decodings[idx]
        pseudocode = pseudocode_encoding_list[idx]
        # pseudocode = pseudocode_encoding_dict[problem]
        code_blocks = extract_code_blocks(decoding) #[TO DO]: I think this is needed? but not sure
        if len(code_blocks) == 0:
            code_blocks = decoding # in case the prompt didn't output ```python``` formatting, is this the best way to do this?
        # print('code blocks in gen_multi_chat_decodings(): ', code_blocks)
        code = textwrap.dedent(code_blocks[0])
        # code = textwrap.dedent(decoding)
        code_decodings_list.append(code)

        new_task_id = problem.replace("/", "-")
        # code_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "decoded_codes", f"generated_code_{stage}.py")
        # code_file_path = os.path.join(dataset_name, "outputs", timestamp, f"iter_{it}", "decoded_codes", f"{new_task_id}_decoded_code_{stage}.py")
        # with open(code_file_path, 'w') as file:
        #     file.write(code)
        # code_file_path_list.append(code_file_path)
        task_pseudocodes_codes[problem] = {"pseudocode": pseudocode, "decoded_code": code}

        # decoding_prompt_file_path = os.path.join(problem_file_path, "outputs", timestamp, f"iter_{it}", "prompts", f"{stage}_stage_decoding_prompt.txt")

    return code_decodings_list, task_pseudocodes_codes

def evaluate_classifier_prompt_test(test_set_filename, prompt, client):
    true_positives = []
    true_negatives = []
    num_problems = 0
    true_negative_errors = {}

    metrics = {}

    task_ids = set()

    for problem in read_jsonl(test_set_filename):
        num_problems += 1
        task_id = problem["task_id"]
        task_ids.add(task_id)
        metrics[task_id] = {"accuracy_score": 0, "true_positive": 0, "true_negative": 0, "near_miss": 0, "cosmetic": 0 }

        pseudocode_dataset = problem["pseudocode_dataset"]
        for entry in pseudocode_dataset:
            if entry["label"] == "true_positive":
                entry["task_id"] = task_id
                true_positives.append(entry)
                true_positive_pseudocode = entry["pseudocode"]
            if entry["label"] == "true_negative":
                entry["task_id"] = task_id
                # entry["true_positive"] = true_positive_pseudocode
                true_negatives.append(entry)

                # error_string = entry["error_string"]
                error_string = entry["error"]
                true_negative_errors[task_id] = error_string
            

    train_pseudocodes_dataset = true_positives + true_negatives
    # print('train_pseudocodes_dataset:', train_pseudocodes_dataset)

    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    
    pseudocodes = []

    score = 0

    for entry in train_pseudocodes_dataset:
        pseudocodes.append(entry['pseudocode'])
    # Feed problems to prompt
    # let's say num problems = 3
    output_list = gen_classifier_outputs(pseudocodes, prompt, client)
    positives_outputs = output_list[:num_problems] # [:3] [0, 1, 2]
    negatives_outputs = output_list[num_problems:] #[3:6] = [3,4,5]




    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    # print('len of output_list: ', len(output_list))
    mislabeled_positives = []
    mislabeled_negatives = []
    labeled_correctly = []

    mislabeled_positives_task_ids = set()
    mislabeled_negatives_task_ids = set()
    # print('metrics:')
    # print(metrics)
    # print('true positives:')
    # print(true_positives)

    for i in range(len(true_positives)):
        entry = true_positives[i]
        label = entry["score"]
        task_id = entry["task_id"]
        output = positives_outputs[i]
        

        if label == output:
            score += 1
            metrics[task_id]["accuracy_score"] += 1
            metrics[task_id]["true_positive"] += 1
            labeled_correctly.append(entry)
        else:
            mislabeled_positives.append(entry)
            # mislabeled_positives_task_ids.add(task_id)

    print('len of positive mislabeled:', len(mislabeled_positives))

    for i in range(len(true_negatives)):
        entry = true_negatives[i]
        label = entry["score"]
        task_id = entry["task_id"]
        output = negatives_outputs[i]

        if output == 0:
            score += 1
            metrics[task_id]["accuracy_score"] += 1
            metrics[task_id]["true_negative"] += 1
            labeled_correctly.append(entry)
        else:
            mislabeled_negatives.append(entry)
            # mislabeled_negatives_task_ids.add(task_id)

    print('len of negative mislabeled: ', len(mislabeled_negatives))

    # See if the outputs correspond to the actual labels
    # for i in range(len(train_pseudocodes_dataset)):
    #     entry = train_pseudocodes_dataset[i]
    #     label = entry["score"]
    #     output = near_miss_outputs[i]

    #     if output < 1:
    #         score += 1
    #     else:
    #         mislabeled_near_misses.append(entry)
    for task_id in metrics:
        metrics[task_id]["accuracy_score"] /= 2


    final_score = score / (len(train_pseudocodes_dataset)) if train_pseudocodes_dataset else 0

    print("final score: ", final_score)
    # print('final_metrics:')
    # print(final_metrics)
    # return mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics

    metrics = check_if_no_metrics(metrics)
    avg_metrics = average_metrics(metrics)

    avg_metrics['final_score'] = final_score
    avg_metrics['avg_score'] = avg_metrics['accuracy_score']

    return mislabeled_positives, mislabeled_negatives, labeled_correctly, avg_metrics

    return avg_metrics

    return mislabeled_positives, mislabeled_negatives, true_negative_errors, final_score, metrics


def evaluate_classifier_prompt(train_set_filename, prompt, client):
    # Decide whcih problems to feed to the prompt, first half of the positive examples and first half of the negative examples
    # train_pseudocodes_dataset = positive_examples[:len(positive_examples)//2] + negative_examples[:len(negative_examples)//2]
    true_positives = []
    true_negatives = []
    near_misses = []
    cosmetic = []
    num_problems = 0
    true_negative_errors = {}
    near_miss_errors = {}

    metrics = {}

    task_ids = set()

    for problem in read_jsonl(train_set_filename):
        num_problems += 1
        task_id = problem["task_id"]
        task_ids.add(task_id)
        metrics[task_id] = {"accuracy_score": 0, "true_positive": 0, "true_negative": 0, "near_miss": 0, "cosmetic": 0 }

        pseudocode_dataset = problem["pseudocode_dataset"]
        for entry in pseudocode_dataset:
            if entry["label"] == "true_positive":
                entry["task_id"] = task_id
                true_positives.append(entry)
                true_positive_pseudocode = entry["pseudocode"]
            if entry["label"] == "true_negative":
                entry["task_id"] = task_id
                entry["true_positive"] = true_positive_pseudocode
                true_negatives.append(entry)

                # error_string = entry["error_string"]
                error_string = entry["error"]
                true_negative_errors[task_id] = error_string
            elif entry["label"] == "near_miss":
                entry["task_id"] = task_id
                entry["true_positive"] = true_positive_pseudocode
                near_misses.append(entry)

                # error_string = entry["error_string"]
                error_string = entry["error"]
                near_miss_errors[task_id] = error_string
            elif entry["label"] == "cosmetic":
                entry["task_id"] = task_id
                entry["true_positive"] = true_positive_pseudocode
                cosmetic.append(entry)

    train_pseudocodes_dataset = true_positives + true_negatives + cosmetic + near_misses
    # print('train_pseudocodes_dataset:', train_pseudocodes_dataset)

    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    
    pseudocodes = []

    score = 0

    for entry in train_pseudocodes_dataset:
        pseudocodes.append(entry['pseudocode'])

    # true_negative_pseudocodes = pseudocodes[2*num_problems:3*num_problems]
    # near_miss_pseudocodes = pseudocodes[3*num_problems:]

    # pseudocode_encoding_list = true_negative_pseudocodes + near_miss_pseudocodes

    # _, true_negative_task_pseudocodes_codes = gen_multi_chat_decodings(dataset_name, task_ids, decoder_prompt, true_negative_pseudocodes, "classifier", timestamp, it, client)
    # results, true_negative_errors = evaluate_functional_correctness(train_set_filename, true_negative_task_pseudocodes_codes)

    # _, near_miss_task_pseudocodes_codes = gen_multi_chat_decodings(dataset_name, task_ids, decoder_prompt, near_miss_pseudocodes, "classifier", timestamp, it, client)
    # results, near_miss_errors = evaluate_functional_correctness(train_set_filename, near_miss_task_pseudocodes_codes)


    # print('len of pseudocodes: ', len(pseudocodes))

    # Feed problems to prompt
    # let's say num problems = 3
    output_list = gen_classifier_outputs(pseudocodes, prompt, client)
    positives_outputs = output_list[:num_problems] # [:3] [0, 1, 2]
    negatives_outputs = output_list[num_problems:2*num_problems] #[3:6] = [3,4,5]
    if 'HumanEval' in train_set_filename:
        cosmetic_outputs = []
        near_miss_outputs = []
    else:
        cosmetic_outputs = output_list[2*num_problems:3*num_problems] #[6,9] = [6, 7, 8]
        near_miss_outputs = output_list[3*num_problems:] #[9:] = [9, 10, 11]

        print("near_miss_outputs:")
        print(near_miss_outputs)




    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    # print('len of output_list: ', len(output_list))
    mislabeled_positives = []
    mislabeled_cosmetic =[]
    mislabeled_negatives = []
    mislabeled_near_misses = []
    labeled_correctly = []


    mislabeled_positives_task_ids = set()
    mislabeled_cosmetic_task_ids = set()
    mislabeled_negatives_task_ids = set()
    mislabeled_near_misses_task_ids = set()
    # print('metrics:')
    # print(metrics)
    # print('true positives:')
    # print(true_positives)

    for i in range(len(true_positives)):
        entry = true_positives[i]
        label = entry["score"]
        task_id = entry["task_id"]
        output = positives_outputs[i]
        

        if label == output:
            score += 1
            metrics[task_id]["accuracy_score"] += 1
            metrics[task_id]["true_positive"] += 1
            labeled_correctly.append(entry)
        else:
            mislabeled_positives.append(entry)
            # mislabeled_positives_task_ids.add(task_id)

    print('len of positive mislabeled:', len(mislabeled_positives))

    for i in range(len(cosmetic)):
        entry = cosmetic[i]
        label = entry["score"]
        task_id = entry["task_id"]
        output = cosmetic_outputs[i]

        if label == output:
            # score += 1
            metrics[task_id]["accuracy_score"] += 1
            metrics[task_id]["cosmetic"] += 1
            labeled_correctly.append(entry)
        else:
            mislabeled_cosmetic.append(entry)
            # mislabeled_cosmetic_task_ids.add(task_id)

    print('len of cosmetic mislabeled: ', len(mislabeled_cosmetic))

    for i in range(len(true_negatives)):
        entry = true_negatives[i]
        label = entry["score"]
        task_id = entry["task_id"]
        output = negatives_outputs[i]

        if label == output:
            score += 1
            metrics[task_id]["accuracy_score"] += 1
            metrics[task_id]["true_negative"] += 1
            labeled_correctly.append(entry)
        else:
            mislabeled_negatives.append(entry)
            # mislabeled_negatives_task_ids.add(task_id)

    print('len of negative mislabeled: ', len(mislabeled_negatives))

    for i in range(len(near_misses)):
        entry = near_misses[i]
        label = entry["score"]
        task_id = entry["task_id"]
        output = near_miss_outputs[i]

        if output == 0:
            # score += 1
            metrics[task_id]["accuracy_score"] += 1
            metrics[task_id]["near_miss"] += 1
            labeled_correctly.append(entry)
        else:
            mislabeled_near_misses.append(entry)
            # mislabeled_near_misses_task_ids.add(task_id)

    print('len of near miss mislabeled: ', len(mislabeled_near_misses))

    # See if the outputs correspond to the actual labels
    # for i in range(len(train_pseudocodes_dataset)):
    #     entry = train_pseudocodes_dataset[i]
    #     label = entry["score"]
    #     output = near_miss_outputs[i]

    #     if output < 1:
    #         score += 1
    #     else:
    #         mislabeled_near_misses.append(entry)
    for task_id in metrics:
        if 'HumanEval' in train_set_filename:
            metrics[task_id]["accuracy_score"] /= 2 # don't do near_miss or cosmetic for HumanEval
        else:
            metrics[task_id]["accuracy_score"] /= 4

    # final_metrics = {task : {"accuracy_score" : metrics[task]["accuracy_score"] / 4 } for task in task_ids}
    # mislabeled_intersection = mislabeled_positives_task_ids.intersection(mislabeled_cosmetic_task_ids, mislabeled_negatives_task_ids, mislabeled_near_misses_task_ids)
    # mislabeled_problems = {problem: [] for problem in mislabeled_intersection}
    # print('len of mislabeled intersection: ', len(mislabeled_intersection))

    # for i in range(len(true_positives)):
    #     entry = true_positives[i]
    #     task_id = entry["task_id"]        

    #     if task_id in mislabeled_intersection:
    #         mislabeled_problems[task_id].append(entry)

    # for i in range(len(cosmetic)):
    #     entry = cosmetic[i]
    #     task_id = entry["task_id"]

    #     if task_id in mislabeled_intersection:
    #         mislabeled_problems[task_id].append(entry)

    # for i in range(len(true_negatives)):
    #     entry = true_negatives[i]
    #     task_id = entry["task_id"]

    #     if task_id in mislabeled_intersection:
    #         mislabeled_problems[task_id].append(entry)

    # for i in range(len(near_misses)):
    #     entry = near_misses[i]
    #     task_id = entry["task_id"]

    #     if task_id in mislabeled_intersection:
    #         mislabeled_problems[task_id].append(entry)
    if 'HumanEval' in train_set_filename:
        final_score = score / (len(train_pseudocodes_dataset)) if train_pseudocodes_dataset else 0
    else: 
        final_score = score / (len(train_pseudocodes_dataset)/2) if train_pseudocodes_dataset else 0

    print("final score: ", final_score)
    # print('final_metrics:')
    # print(final_metrics)
    # return mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics

    return mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, labeled_correctly, true_negative_errors, near_miss_errors, final_score, metrics

def evaluate_classifier_prompt_v2(positive_examples, negative_examples, prompt, client):
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

    return score / len(train_pseudocodes_dataset) if train_pseudocodes_dataset else 0

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

def write_error_strings_to_file(file_name, new_file_name, decoder_prompt, client):
    true_positives = []
    true_negatives = []
    near_misses = []
    cosmetic = []
    task_ids = set()
    
    for problem in read_jsonl(file_name):
        task_id = problem["task_id"]
        task_ids.add(task_id)

        pseudocode_dataset = problem["pseudocode_dataset"]
        for entry in pseudocode_dataset:
            # if entry["label"] == "true_positive":
            #     new_entry = entry
            #     new_entry["task_id"] = task_id
            #     true_positives.append(new_entry)
            if entry["label"] == "true_negative":
                new_entry = entry
                new_entry["task_id"] = task_id
                true_negatives.append(new_entry)
            elif entry["label"] == "near_miss":
                new_entry = entry
                new_entry["task_id"] = task_id
                near_misses.append(new_entry)
            # elif entry["label"] == "cosmetic":
            #     new_entry = entry
            #     new_entry["task_id"] = task_id
            #     cosmetic.append(new_entry)

    # train_pseudocodes_dataset = true_positives + cosmetic + true_negatives + near_misses
    # print('train_pseudocodes_dataset:', train_pseudocodes_dataset)

    # print('len of train_pseudocodes_dataset: ', len(train_pseudocodes_dataset))
    
    pseudocodes = []

    true_negative_pseudocodes = []
    near_miss_pseudocodes = []

    for entry in true_negatives:
        true_negative_pseudocodes.append(entry['pseudocode'])

    for entry in near_misses:
        near_miss_pseudocodes.append(entry['pseudocode'])

    # pseudocode_encoding_list = true_negative_pseudocodes + near_miss_pseudocodes
    dataset_name = "classifier_pseudocodes"
    _, true_negative_task_pseudocodes_codes = gen_multi_chat_decodings(dataset_name, task_ids, decoder_prompt, true_negative_pseudocodes, "classifier", "00-00-00_00-00-00", 0, client)
    results, true_negative_errors = evaluate_functional_correctness(file_name, true_negative_task_pseudocodes_codes)

    _, near_miss_task_pseudocodes_codes = gen_multi_chat_decodings(dataset_name, task_ids, decoder_prompt, near_miss_pseudocodes, "classifier", "00-00-00_00-00-00", 0, client)
    results, near_miss_errors = evaluate_functional_correctness(file_name, near_miss_task_pseudocodes_codes)

    results = []
    num_errors_shown = 1
    for problem in read_jsonl(file_name):
        task_id = problem["task_id"]

        pseudocode_dataset = problem["pseudocode_dataset"]
        for entry in pseudocode_dataset:
            if entry["label"] == "true_negative":
                test_errors = true_negative_errors[task_id]
                if test_errors:
                    error_string = str(test_errors[:num_errors_shown])
                    entry["error_string"] = error_string
                else:
                    entry["error_string"] = ''
                
            elif entry["label"] == "near_miss":
                test_errors = near_miss_errors[task_id]
                if test_errors:
                    error_string = str(test_errors[:num_errors_shown])
                    entry["error_string"] = error_string
                else:
                    entry["error_string"] = ''
        results.append(problem)

    write_jsonl(new_file_name, results)

def reformat_human_eval_file(file_name):
    results = []
    for problem in read_jsonl(file_name):
        task_id = problem["task_id"]
        task_id = task_id.replace("/", "-")
        problem["task_id"] = task_id
        results.append(problem)

    write_jsonl(file_name, results)

def print_feedback_from_file(file_name_json):
    if os.path.exists(file_name_json):
        with open(file_name_json, "r") as f:
            results = json.load(f)

    print('feedback:')
    print(results['feedback'])

def write_classifier_pseudocodes_to_file(labeled_pseudocode, pseudocode_path):
    positives = []
    negatives = []
    near_misses = []
    cosmetic = []
    for entry in labeled_pseudocode:
        label = entry["label"]
        new_entry = {"task_id": entry["task_id"]}
        for key, value in entry.items():
            if key != "task_id":
                new_entry[key] = value
        if entry["label"] == "true_positive":
            positives.append(new_entry)
        elif entry["label"] == "true_negative":
            negatives.append(new_entry)
        elif entry["label"] == "near_miss":
            near_misses.append(new_entry)
        elif entry["label"] == "cosmetic":
            cosmetic.append(new_entry)

    positives_jsonl_name = os.path.join(pseudocode_path, "positives.jsonl")
    write_jsonl(positives_jsonl_name, positives)

    negatives_jsonl_name = os.path.join(pseudocode_path, "negatives.jsonl")
    write_jsonl(negatives_jsonl_name, negatives)

    if near_misses:
        near_misses_jsonl_name = os.path.join(pseudocode_path, "near_misses.jsonl")
        write_jsonl(near_misses_jsonl_name, near_misses)

    if cosmetic:
        cosmetic_jsonl_name = os.path.join(pseudocode_path, "cosmetic.jsonl")
        write_jsonl(cosmetic_jsonl_name, cosmetic)

    positives_pseudocodes_path = Path(os.path.join(pseudocode_path), "positives")
    positives_pseudocodes_path.mkdir(parents=True, exist_ok=True)

    negatives_pseudocodes_path = Path(os.path.join(pseudocode_path), "negatives")
    negatives_pseudocodes_path.mkdir(parents=True, exist_ok=True)

    if near_misses:
        near_misses_pseudocodes_path = Path(os.path.join(pseudocode_path), "near_misses")
        near_misses_pseudocodes_path.mkdir(parents=True, exist_ok=True)

    if cosmetic:
        cosmetic_pseudocodes_path = Path(os.path.join(pseudocode_path), "cosmetic")
        cosmetic_pseudocodes_path.mkdir(parents=True, exist_ok=True)

    for entry in read_jsonl(positives_jsonl_name):
        task_id = entry["task_id"]
        pseudocode = entry["pseudocode"]
        pseudocode_path_name = os.path.join(positives_pseudocodes_path, f'{task_id}.txt')
        with open(pseudocode_path_name, 'w') as file:
            file.write(pseudocode)

    for entry in read_jsonl(negatives_jsonl_name):
        task_id = entry["task_id"]
        pseudocode = entry["pseudocode"]
        pseudocode_path_name = os.path.join(negatives_pseudocodes_path, f'{task_id}.txt')
        with open(pseudocode_path_name, 'w') as file:
            file.write(pseudocode)

    if near_misses:
        for entry in read_jsonl(near_misses_jsonl_name):
            task_id = entry["task_id"]
            pseudocode = entry["pseudocode"]
            pseudocode_path_name = os.path.join(near_misses_pseudocodes_path, f'{task_id}.txt')
            with open(pseudocode_path_name, 'w') as file:
                file.write(pseudocode)

    if cosmetic:
        for entry in read_jsonl(cosmetic_jsonl_name):
            task_id = entry["task_id"]
            pseudocode = entry["pseudocode"]
            pseudocode_path_name = os.path.join(cosmetic_pseudocodes_path, f'{task_id}.txt')
            with open(pseudocode_path_name, 'w') as file:
                file.write(pseudocode)

def organize_pseudocode(dir_path_name, timestamp, iter_to_organize, problems_filename, stage):
    problems = list_jsonl_task_ids(problems_filename)

    metrics_path = os.path.join(dir_path_name, "metrics", f'{timestamp}_metrics.json' )
    outputs_path = os.path.join(dir_path_name, "outputs", timestamp, f'iter_{iter_to_organize}', "pseudocodes")

    positives_pseudocodes_path = Path(os.path.join(outputs_path), "positives")
    positives_pseudocodes_path.mkdir(parents=True, exist_ok=True)

    negatives_pseudocodes_path = Path(os.path.join(outputs_path), "negatives")
    negatives_pseudocodes_path.mkdir(parents=True, exist_ok=True)
    
    near_misses_pseudocodes_path = Path(os.path.join(outputs_path), "near_misses")
    near_misses_pseudocodes_path.mkdir(parents=True, exist_ok=True)

    positives = []
    negatives = []
    near_misses = []

    positives_task_ids = []
    negatives_task_ids = []
    near_misses_task_ids = []

    near_miss_threshold = 0.8

    with open(metrics_path, 'r') as file:
        metrics_data = json.load(file)

    for i in range(len(metrics_data)-1, -1, -1): # how to iterate? i suppose starting from the back to get the best ones? with the most iterations?
        entry = metrics_data[i]
        current_iter = entry["iter"]

        if current_iter == iter_to_organize:
            for problem in problems:
                old_pseudocode_path = os.path.join(outputs_path, f'{problem}_pseudocode_{stage}.txt')

                if entry[f"{problem}_passing_rate"] == 1.0: # per set I only want one problem
                    new_pseudocode_path = os.path.join(positives_pseudocodes_path, f'{problem}.txt')

                    with open(old_pseudocode_path, 'r') as old_file, open(new_pseudocode_path, 'w') as new_file:
                        pseudocode = old_file.read()
                        new_file.write(pseudocode)

                    new_entry = {'task_id': problem, 'passing_rate': entry[f"{problem}_passing_rate"], 'pseudocode': pseudocode}
                    positives.append(new_entry)

                    positives_task_ids.append(problem)
                elif entry[f"{problem}_passing_rate"] >= near_miss_threshold:                    
                    new_pseudocode_path = os.path.join(near_misses_pseudocodes_path, f'{problem}.txt')

                    with open(old_pseudocode_path, 'r') as old_file, open(new_pseudocode_path, 'w') as new_file:
                        pseudocode = old_file.read()
                        new_file.write(pseudocode)

                    new_entry = {'task_id': problem, 'passing_rate': entry[f"{problem}_passing_rate"], 'pseudocode': pseudocode}
                    near_misses.append(new_entry)

                    near_misses_task_ids.append(problem)
                else:
                    new_pseudocode_path = os.path.join(negatives_pseudocodes_path, f'{problem}.txt')

                    with open(old_pseudocode_path, 'r') as old_file, open(new_pseudocode_path, 'w') as new_file:
                        pseudocode = old_file.read()
                        new_file.write(pseudocode)

                    new_entry = {'task_id': problem, 'passing_rate': entry[f"{problem}_passing_rate"], 'pseudocode': pseudocode}
                    negatives.append(new_entry)

                    negatives_task_ids.append(problem)

    if positives:
        positives_jsonl_name = os.path.join(positives_pseudocodes_path, "positives.jsonl")
        write_jsonl(positives_jsonl_name, positives)

        positives_task_ids_file_name = os.path.join(positives_pseudocodes_path, "positives_task_ids.txt")
        task_ids = '\n'.join(positives_task_ids)
        with open(positives_task_ids_file_name, 'w') as file:
            file.write(task_ids)

    if negatives:
        negatives_jsonl_name = os.path.join(negatives_pseudocodes_path, "negatives.jsonl")
        write_jsonl(negatives_jsonl_name, negatives)

        negatives_task_ids_file_name = os.path.join(negatives_pseudocodes_path, "negatives_task_ids.txt")
        task_ids = '\n'.join(negatives_task_ids)
        with open(negatives_task_ids_file_name, 'w') as file:
            file.write(task_ids)

    if near_misses:
        near_misses_jsonl_name = os.path.join(near_misses_pseudocodes_path, "near_misses.jsonl")
        write_jsonl(near_misses_jsonl_name, near_misses)

        near_misses_task_ids_file_name = os.path.join(near_misses_pseudocodes_path, "near_misses_task_ids.txt")
        task_ids = '\n'.join(near_misses_task_ids)
        with open(near_misses_task_ids_file_name, 'w') as file:
            file.write(task_ids)

def get_intersection_of_pseudocodes(dir_path_name, timestamp, first_iter, second_iter, problems_filename):

    first_outputs_path = os.path.join(dir_path_name, "outputs", timestamp, f'iter_{first_iter}', "pseudocodes")
    second_outputs_path = os.path.join(dir_path_name, "outputs", timestamp, f'iter_{second_iter}', "pseudocodes")

    first_positives_pseudocodes_path = os.path.join(first_outputs_path, "positives", "positives_task_ids.txt")
    first_negatives_pseudocodes_path = os.path.join(first_outputs_path, "negatives", "negatives_task_ids.txt")
    
    second_positives_pseudocodes_path = os.path.join(second_outputs_path, "positives", "positives_task_ids.txt")
    second_negatives_pseudocodes_path = os.path.join(second_outputs_path, "negatives", "negatives_task_ids.txt")

    with open(first_positives_pseudocodes_path, 'r') as file:
        first_positives_task_ids = set(file.read().split())
    with open(first_negatives_pseudocodes_path, 'r') as file:
        first_negatives_task_ids = set(file.read().split())

    with open(second_positives_pseudocodes_path, 'r') as file:
        second_positives_task_ids = set(file.read().split())
    with open(second_negatives_pseudocodes_path, 'r') as file:
        second_negatives_task_ids = set(file.read().split())

    print('intersection of first positives with second negatives')
    print(first_positives_task_ids.intersection(second_negatives_task_ids))

    print('intersection of second positives with first negatives')
    print(second_positives_task_ids.intersection(first_negatives_task_ids))


    


 