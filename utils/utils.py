import logging
import re
import os
import inspect
import hydra
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path


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
def setup_dataset(timestamp, problems_dir, iterations): # [TO DO]: this needs to be edited!!! for sure. actually i don't need this... 
    base_directory = Path(problems_dir)
    # runs_path = base_directory / "runs"
    # runs_path.mkdir(parents=True, exist_ok=True) 
    # timestamp_path = base_directory / "runs" / timestamp
    # timestamp_path.mkdir(parents=True, exist_ok=True) 

    outputs_path = base_directory / "outputs"
    timestamp_path = outputs_path / timestamp

    outputs_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{outputs_path}' created successfully")
    timestamp_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{timestamp_path}' created successfully")

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

    for it in range(iterations):
        iter_path = timestamp_path / f"iter_{it+1}"
        iter_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{iter_path}' created successfully")

        previous_best_path = iter_path / "previous_best"
        pseudocodes_path = iter_path / "pseudocodes"
        results_path = iter_path / "results"
        codes_path = iter_path / "decoded_codes"
        # metrics_path = iter_path / "metrics"
        errors_path = iter_path / "errors"
        prompts_path = iter_path / "prompts"

        previous_best_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{stdouts_path}' created successfully")
        pseudocodes_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{pseudocodes_path}' created successfully")
        results_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{results_path}' created successfully")
        codes_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{codes_path}' created successfully")
        # metrics_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{metrics_path}' created successfully")
        errors_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{errors_path}' created successfully")
        prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
        # print(f"Directory '{prompts_path}' created successfully")
            
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

def minify_code(problems_dir):
    base_directory = Path(problems_dir)

    for problem in base_directory.iterdir():
        if problem.is_dir() and problem.name != 'metrics':
            code_path = problem / "llm_scripting" / "starter_code.py"
            minified_code_path = problem / "llm_scripting" / "minified_code.py"
            starter_code = file_to_string(str(code_path))
            minified_code = minify(starter_code, rename_locals=True, remove_annotations=True, remove_literal_statements=True)
            with open(str(minified_code_path), 'w') as file:
                file.write(minified_code)

