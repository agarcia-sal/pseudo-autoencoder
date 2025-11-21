import logging
import re
import os
import shutil
import inspect
import hydra
import json
import matplotlib.pyplot as plt
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

from evaluation.eval_dataset.data import read_jsonl, write_jsonl


load_dotenv()

def init_client(cfg):
    global client
    if cfg.get("model", None): # for compatibility
        model: str = cfg.get("model")
        temperature: float = cfg.get("temperature", 1.0)
        if model.startswith("gpt"):
            from utils.llm_client.openai import OpenAIClient
            client = OpenAIClient(model, temperature)
    else:
        client = hydra.utils.instantiate(cfg.llm_client)
    return client
    

def file_to_string(filename):
    with open(filename, 'r') as file:
        return file.read()

def filter_traceback(s):
    lines = s.split('\n')
    filtered_lines = []
    for i, line in enumerate(lines):
        if line.startswith('Traceback'):
            for j in range(i, len(lines)):
                if "Set the environment variable HYDRA_FULL_ERROR=1" in lines[j]:
                    break
                filtered_lines.append(lines[j])
            return '\n'.join(filtered_lines)
    return ''  # Return an empty string if no Traceback is found

def block_until_running(stdout_filepath, log_status=False, iter_num=-1, response_id=-1):
    # Ensure that the evaluation has started before moving on
    while True:
        log = file_to_string(stdout_filepath)
        if  len(log) > 0:
            if log_status and "Traceback" in log:
                logging.info(f"Iteration {iter_num}: Code Run {response_id} execution error!")
            else:
                logging.info(f"Iteration {iter_num}: Code Run {response_id} successful!")
            break


def extract_description(response: str) -> tuple[str, str]:
    # Regex patterns to extract code description enclosed in GPT response, it starts with ‘<start>’ and ends with ‘<end>’
    pattern_desc = [r'<start>(.*?)```python', r'<start>(.*?)<end>']
    for pattern in pattern_desc:
        desc_string = re.search(pattern, response, re.DOTALL)
        desc_string = desc_string.group(1).strip() if desc_string is not None else None
        if desc_string is not None:
            break
    return desc_string


def extract_code_from_generator(content):
    """Extract code from the response of the code generator."""
    pattern_code = r'```python(.*?)```'
    code_string = re.search(pattern_code, content, re.DOTALL)
    code_string = code_string.group(1).strip() if code_string is not None else None
    if code_string is None:
        # Find the line that starts with "def" and the line that starts with "return", and extract the code in between
        lines = content.split('\n')
        start = None
        end = None
        for i, line in enumerate(lines):
            if line.startswith('def'):
                start = i
            if 'return' in line:
                end = i
                break
        if start is not None and end is not None:
            code_string = '\n'.join(lines[start:end+1])
    
    if code_string is None:
        return None
    # Add import statements if not present
    if "np" in code_string:
        code_string = "import numpy as np\n" + code_string
    if "torch" in code_string:
        code_string = "import torch\n" + code_string
    if "sys" in code_string: # had to add this one, even though i do not want to 
        code_string = "import sys\n" + code_string 
    return code_string


def filter_code(code_string):
    """Remove lines containing signature and import statements."""
    lines = code_string.split('\n')
    filtered_lines = []
    for line in lines:
        # if line.startswith('def'):
        #     continue
        # if line.startswith('import'):
        #     continue
        if line.startswith('import numpy'):
            continue
        # elif line.startswith('from'):
        #     continue
        elif line.startswith('assert'): #added this check
            continue
        # elif line.startswith('return'):
        #     filtered_lines.append(line)
        #     break
        else:
            filtered_lines.append(line)
    code_string = '\n'.join(filtered_lines)
    return code_string


def get_heuristic_name(module, possible_names: list[str]):
    for func_name in possible_names:
        if hasattr(module, func_name):
            if inspect.isfunction(getattr(module, func_name)):
                return func_name
            
# what i added:
            
def get_line_count(code_string):
    lines = code_string.split('\n')
    return len(lines)
            
def run_prompt_pseudocode_to_code(prompt):
    print("in run_prompt_pseudocode_to_code")
    # prompt = prompt.format(
    #     pseudocode = get_pseudocode()
    # ) + '\nOutput code only and enclose your code with Python code block: ```python ... ```'
    prompt += '\nOutput code only and enclose your code with Python code block: ```python ... ```'
    client = OpenAI(
        # This is the default and can be omitted
        # api_key=os.environ.get("OPENAI_API_KEY"),
        # api_key=api_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
    )

    code = response.choices[0].message.content
    return code
# def format_seed_func(prompt):
#     return prompt.format(
#         pseudocode=get_pseudocode()
#     )
def set_up_dataset(timestamp, problems_dir, iterations): # [TO DO]: this needs to be edited!!! for sure. actually i don't need this... 
    base_directory = Path(problems_dir)
    # runs_path = base_directory / "runs"
    # runs_path.mkdir(parents=True, exist_ok=True) 
    # timestamp_path = base_directory / "runs" / timestamp
    # timestamp_path.mkdir(parents=True, exist_ok=True) 

    outputs_path = base_directory / "outputs"
    timestamp_path = outputs_path / timestamp

    train_path = outputs_path / "train"
    test_path = outputs_path / "test"

    outputs_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{outputs_path}' created successfully")
    timestamp_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{timestamp_path}' created successfully")
    train_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{train_path}' created successfully")
    test_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{test_path}' created successfully")

    # for problem in base_directory.iterdir():
    #     if problem.is_dir() and problem.name != 'metrics':
    #         outputs_path = problem / "outputs"
    #         timestamp_path = outputs_path / timestamp
            # stdouts_path = outputs_path / "stdouts"
            # pseudocodes_path = outputs_path / "pseudocodes"
            # results_path = outputs_path / "results"
            # codes_path = outputs_path / "decoded_codes"
            # metrics_path = outputs_path / "metrics"
            # errors_path = outputs_path / "errors"

            # outputs_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{outputs_path}' created successfully")
            # timestamp_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{timestamp_path}' created successfully")

    archive_paths = [train_path, test_path, timestamp_path]

    for it in range(iterations):
        for arch_path in archive_paths:
            iter_path = arch_path / f"iter_{it+1}"
            iter_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{iter_path}' created successfully")

            previous_best_path = iter_path / "previous_best"
            pseudocodes_path = iter_path / "pseudocodes"
            # results_path = iter_path / "results"
            codes_path = iter_path / "decoded_codes"
            # metrics_path = iter_path / "metrics"
            errors_path = iter_path / "errors"
            prompts_path = iter_path / "prompts"
            

            previous_best_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{stdouts_path}' created successfully")
            pseudocodes_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{pseudocodes_path}' created successfully")
            # results_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{results_path}' created successfully")
            codes_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{codes_path}' created successfully")
            errors_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{errors_path}' created successfully")
            prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{prompts_path}' created successfully")

            output_paths = [pseudocodes_path, codes_path, errors_path]

            for path in output_paths:


                if 'classifier' in problems_dir:
                    success_path = path / "pass"
                    failure_path = path / "fail"

                    success_path.mkdir(parents=True, exist_ok=True)
                    failure_path.mkdir(parents=True, exist_ok=True)
                elif 'autoencoder' in problems_dir:
                    positives_path = path / "positives"
                    near_misses_path = path / "near_misses"
                    negatives_path = path / "negatives"

                    positives_path.mkdir(parents=True, exist_ok=True)
                    near_misses_path.mkdir(parents=True, exist_ok=True)
                    negatives_path.mkdir(parents=True, exist_ok=True)
                
            # near_miss_path.mkdir(parents=True, exist_ok=True)
            
            ##### Make timestamps:
            # pseudocodes_timestamp = pseudocodes_path / timestamp
            # codes_timestamp = codes_path / timestamp
            # metrics_timestamp = metrics_path / timestamp
            # errors_timestamp = errors_path / timestamp

            # pseudocodes_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{pseudocodes_timestamp}' created successfully")
            # codes_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{codes_timestamp}' created successfully")
            # metrics_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{metrics_timestamp}' created successfully")
            # errors_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            # print(f"Directory '{metrics_timestamp}' created successfully")

    overall_metrics_path = base_directory / "metrics"
    overall_metrics_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{overall_metrics_path}' created successfully")

def set_up_codebase(ROOT_DIR):
    base_directory = Path(ROOT_DIR)
    data_path = base_directory / "data"

    outputs_path = base_directory / "outputs"
    figures_path = outputs_path / "figures"
    prompts_path = outputs_path / "prompts"

    data_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{data_path}' created successfully")
    outputs_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{outputs_path}' created successfully")
    figures_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{figures_path}' created successfully")
    prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{prompts_path}' created successfully")

    pipeline_list = ['autoencoder', 'cosmetic', 'classifier']

    for pipeline in pipeline_list:
        pipeline_path = data_path / pipeline
        leet_code_path = pipeline_path / "leet_code"
        human_eval_path = pipeline_path / "human_eval"

        pipeline_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        print(f"Directory '{pipeline_path}' created successfully")
        leet_code_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        print(f"Directory '{leet_code_path}' created successfully")
        human_eval_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        print(f"Directory '{human_eval_path}' created successfully")


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

def reformat_human_eval_file(file_name):
    results = []
    for problem in read_jsonl(file_name):
        task_id = problem["task_id"]
        new_task_id = task_id.replace("/", "-")
        problem["task_id"] = new_task_id
        results.append(problem)

    write_jsonl(file_name, results)

def print_feedback_from_file(file_name_json):
    if os.path.exists(file_name_json):
        with open(file_name_json, "r") as f:
            results = json.load(f)

    print('feedback:')
    print(results['feedback'])

def preprocess_data(ROOT_DIR):
    '''
    This function will perform the following operations:
    1. Take LeetCodeDataset-v0.3.0 and return only 50% medium difficulty and 50% hard difficulty as a new dataset called
    LeetCodeDataset-v0.3.5 for both the train and test split
    2. Reformat HumanEval file so that task ids contain '-' instead of '/'
    '''
    # LeetCode reformatting
    problems_dir = os.path.join(ROOT_DIR, "data", "autoencoder", "leet_code")
    size_limits = [800, 200]
    splits = ['train', 'test']

    for limit, split in zip(size_limits, splits):
        difficulty_map = {"Hard": limit / 2, "Medium": limit / 2 }
        problems_file_name = os.path.join(problems_dir, f'LeetCodeDataset-v0.3.0-{split}.jsonl')
        new_file_name = os.path.join(problems_dir, f'LeetCodeDataset-v0.3.5-{split}.jsonl')
        if os.path.exists(problems_file_name):
            copy_difficulty_problems(problems_file_name, new_file_name, difficulty_map, limit)

    # Create HumanEval train and test splits
    idx = 1
    result_train = []
    result_test = []
    problems_file_name = os.path.join(ROOT_DIR, "data", "autoencoder", "human_eval", 'HumanEval.jsonl')
    new_file_name_train = os.path.join(ROOT_DIR, "data", "autoencoder", "human_eval", 'HumanEval-train.jsonl')
    new_file_name_test = os.path.join(ROOT_DIR, "data", "autoencoder", "human_eval", 'HumanEval-test.jsonl')

    if os.path.exists(problems_file_name):
        for problem in read_jsonl(problems_file_name):
            if idx < 135:
                result_train.append(problem)
            else:
                result_test.append(problem)
            idx += 1
        write_jsonl(new_file_name_train, result_train)
        write_jsonl(new_file_name_test, result_test)

    # HumanEval reformatting to replace task ids '/' with '-'
    problems_dir = os.path.join(ROOT_DIR, "data", "autoencoder", "human_eval")
    for split in splits:
        problems_file_name = f'HumanEval-{split}.jsonl'
        file_name = os.path.join(problems_dir, problems_file_name)
        if os.path.exists(file_name):
            reformat_human_eval_file(file_name)

def plot_pipeline(cfg, ROOT_DIR, timestamp, pipeline):
    problems_dir_name = 'leet_code'
    # [TO DO]: figure out what to do about the timestamps for autoencoder and classifier cause they might be the same
    # ^ can't be the same because then the data class doesn't work
    problem_metrics_file = os.path.join(ROOT_DIR, "data", pipeline, cfg.dataset, "metrics", f"{timestamp}_metrics.json")
    with open(problem_metrics_file, "r") as f:
        data = json.load(f)
    df_pipeline = pd.DataFrame(data)

    label = ''
    metrics = []
    if cfg.dataset == 'leet_code':
        label = "LeetCode"
    elif cfg.dataset == 'human_eval':
        label = "HumanEval"

    agent = ''
    if cfg.algorithm == 'greedy':
        agent = 'GreedyRefinenment'
    elif cfg.algorithm == 'direct_answer':
        agent = 'DirectAnswer'

    table_values = {}
    if pipeline == 'autoencoder': # [TO DO]: change readability metric
        metrics = ['avg_score', 'passing_rate', cfg.readability_metric]
        last_row = df_pipeline.iloc[-1]
        table_values = {metric: last_row[metric] for metric in metrics}

    elif pipeline == 'classifier':
        metrics = ['classifier_score_train', 'classifier_score_val', 'classifier_score_test']
        for idx in range(-3, 0):
            row = df_pipeline.iloc[idx]
            metric = metrics[idx]
            table_values[metric] = row["avg_score"]

    # print('table_values:')
    # print(table_values)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')

    table_data = []
    for metric in metrics:
        table_data.append([metric, f"{table_values[metric]:.3f}"])

    table = ax.table(cellText=table_data,
                    colLabels=['Metric', f'{label}'],
                    cellLoc='center',
                    loc='center',
                    colColours=['#f0f0f0', '#d0e5ff'])

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    plt.title(f'Metric Values for {label} Dataset with {agent} Agent', fontsize=14)
    plt.savefig(os.path.join(ROOT_DIR, "outputs", "figures", f"{pipeline}_{timestamp}.png"), bbox_inches='tight', dpi=300)
    
def empty_folder(folder_path):
    """
    Empties the contents of a specified folder.
    Deletes all files and subdirectories within the folder.
    """
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Remove file or symbolic link
                print(f"Removed file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove subdirectory and its contents
                print(f"Removed directory: {item_path}")
        except OSError as e:
            print(f"Error deleting {item_path}: {e}")

def delete_file(file_path):
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)  # Remove file or symbolic link
        print(f"Removed file: {file_path}")

    



