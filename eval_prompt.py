from dotenv import load_dotenv
import logging 
import re
import subprocess
import os
import time
import json
import matplotlib.pyplot as plt
from openai import OpenAI
import shutil
from pathlib import Path
from datetime import datetime
import sys
from pathlib import Path
sys.path.insert(0, "../")


ROOT_DIR = os.getcwd()

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    api_key = os.getenv('OPENAI_API_KEY'),
)

# Access the variable
api_key = os.getenv('OPENAI_API_KEY')


# Function to get response from OpenAI for each prompt
def get_response(prompt, context=""):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt + context,
            }
        ],
        # model="gpt-4o-mini",
        model='gpt-4.1-mini', #switching to 4o because hit requests per day (RPD) rate limit for 4o-mini
    )
    return chat_completion.choices[0].message.content

def extract_code(response):
    matches = re.findall(r"```(?:\w+)?\n(.*?)```", response, re.DOTALL)
    return "\n\n".join(matches) if matches else response  # Return code if found, else full response



def run_prompts(prompts, context):

    # Start the chain of prompts
    # context = starting_code
    for i, prompt in enumerate(prompts):
        # print(f"Prompt {i + 1}: {prompt}")
        # Get the output and add it to the context
        output = get_response(prompt, context)
        # print(f"Output {i + 1}: {output}")
        
        # Update the context for the next prompt
        context = output + "\n"
    return context

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip newline characters, and store in a set
        temp_list = file.read().split()
        return [elt.strip(' (,)') for elt in temp_list]
        # return list(line.strip() for line in file if line.strip())

def compare_outputs(file_path_expected, file_path_stdout):
    list_expected = read_file_to_list(file_path_expected)
    list_stdout = read_file_to_list(file_path_stdout)
    # print("list expected: ", list_expected)
    # print("list stdout: ", list_stdout)

    if len(list_expected) != len(list_stdout):
        return False
    # smallest_length = min(len(list_expected), len(list_stdout))
    for i in range(len(list_expected)):
        if list_expected[i] != list_stdout[i]:
            return False
        
    return True

def run_test_cases(problem_path, problem_name, problem_script_path, num_test_cases, decoding_prompt_num, trial, timestamp):
    # print('num of test cases: ', num_test_cases)
    num_correct = 0
    num_errors = 0
    for i in range(1, num_test_cases + 1):
        # input_file_path = f"{ROOT_DIR}/problems/hard/{problem_name}/test_cases/{i}_input.txt"
        # output_file_path = f"{ROOT_DIR}/problems/hard/{problem_name}/test_cases/{i}_output.txt"
        # stdout_file_path = f"{ROOT_DIR}/problems/hard/{problem_name}/test_cases/{i}_stdout.txt"

        input_file_path = f"{problem_path}/test_cases/{i}_input.txt"
        output_file_path = f"{problem_path}/test_cases/{i}_output.txt"
        stdout_file_path = f"{problem_path}/outputs/stdouts/{i}_stdout.txt"
        error_file_path = f"{problem_path}/outputs/errors/{timestamp}/decoding_prompt_{decoding_prompt_num}_trial_{trial}_test_case_{i}.txt"
        timeout = 10

        try:

            with open(input_file_path, 'r') as input_file, open(stdout_file_path, 'w') as output_file, open(error_file_path, 'w') as error_file:
                result = subprocess.run(["python3", problem_script_path], stdin=input_file, stdout=output_file, stderr=error_file, timeout=10) #capture stdout and stderr

            # if result.returncode == 0:
            #     print("Script ran successfully.")
            # else:
            #     print("Script failed:", result.stderr)
            if result.returncode != 0:
                print(f"Script failed with return code {result.returncode}. Check the error file at {error_file_path} for details.\n")
                num_errors += 1
                if num_errors == 2:
                    break # if there is an error for one trial, there must be an error for the other trials
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
                num_correct += 1
        except subprocess.TimeoutExpired:
            with open(error_file_path, 'a') as file:
                file.write(f"Script timed out after {timeout} seconds.")
                file.write("------------------------------------------\n")
            num_correct = 0 # if faulty code, none of them are going to pass so break
            print(f"Script timed out after {timeout} seconds.")
            break
        except subprocess.CalledProcessError as e:
            print(f"Script failed with error: {e}")
            with open(error_file_path, 'a') as file:
                file.write("Script failed with error:\n")
                file.write(f"{e}\n")
                file.write("------------------------------------------\n")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            with open(error_file_path, 'a') as file:
                file.write("File not found error:\n")
                file.write(f"{e}\n")
                file.write("------------------------------------------\n")
        except Exception as e:
            print(f"Unexpected error: {e}")
            with open(error_file_path, 'a') as file:
                file.write("Unexpected error:\n")
                file.write(f"{e}\n")
                file.write("------------------------------------------\n")
    print(f"[*] Percentage of test cases passed:")
    print(num_correct/num_test_cases*1.0)
    return num_correct

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

def add_metrics(new_metrics_dict, old_metrics_dict):
    for key, value in new_metrics_dict.items():
        if key not in old_metrics_dict:
            old_metrics_dict[key] = new_metrics_dict[key]
        else:
            old_metrics_dict[key] += new_metrics_dict[key]

    return old_metrics_dict

def get_metrics(stage, final_string, original_code, max_num_test_cases_passed, num_test_cases): #remove 'classifier_label' parameter for now
    # am going to remove the parameter 'metrics_path' for now

    metrics = {
        "line_count": count_lines(original_code),
        "keyword_count": keyword_count(original_code),
        "comment_count": comment_count(original_code),
        "avg_variable_name_length": avg_variable_name_length(original_code),
        "word_count": word_count(original_code),
        # "char_count": char_count(original_code),
        # "max_num_test_cases_passed" : num_test_cases,
        "max_passing_rate" : max_num_test_cases_passed/num_test_cases,
    }

    # if stage == "code":
    #     # difference_metrics["max_num_test_cases_passed"] = final_metrics["max_num_test_cases_passed"]
    #     metrics["max_passing_rate"] = max_num_test_cases_passed/num_test_cases
    return metrics

def save_metrics(avg_metrics, metrics_path, timestamp, stage, round):
    metrics_file_path = f'{metrics_path}/{timestamp}_{stage}_metrics.json' # [TO DO]: create time stamp directory, refactor calculate_metrics i think to only do encoding or decoding metrics
    # Load existing data (if any)
    if os.path.exists(metrics_file_path):
        with open(metrics_file_path, "r") as f:
            results = json.load(f)
    else:
        results = []

    new_result = {key: value for key, value in avg_metrics.items()}
    new_result['round'] = round

        # Append new result
    results.append(new_result)

    # Save updated results
    with open(metrics_file_path, "w") as f:
        json.dump(results, f, indent=2)  # `indent` for readability


def normalize_metrics(metrics, dataset_metrics_dict):
    '''
    Normalize metrics across problems, returns a dataset_dict where the keys are the problems and the values are dictionaries.
    '''
    metrics_min_max = {}
    new_dataset_dict = {}
    problem_count = 0
    # Step 1: get the minimums and maximums of everything
    for problem_name_key in dataset_metrics_dict:
        problem_count += 0 
        for metric_key in metrics:
            metric_value = dataset_metrics_dict[problem_name_key][metric_key]

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
    for problem_name_key in dataset_metrics_dict:
        new_metrics_dict = {}
        for metric_key in metrics:
            metric_value = dataset_metrics_dict[problem_name_key][metric_key]
            x_min = metrics_min_max[metric_key][0]
            x_max = metrics_min_max[metric_key][1]
            if (x_max - x_min) != 0: 
                normalized_value = (metric_value - x_min)/ (x_max - x_min)
            new_metrics_dict[metric_key] = normalized_value
        # print('in normalize_metrics:')
        # print(f'problem: {problem_name_key} has dict: {new_metrics_dict}')
        new_dataset_dict[problem_name_key] = new_metrics_dict

    return new_dataset_dict

def average_metrics(metrics, dataset_metrics_dict):
    '''
    Average the metrics across all problems. Returns a simple metrics dict where the keys are the metrics and the values are numbers
    '''
    problem_count = 0 
    new_metrics_dict = {}

    for problem_name_key in dataset_metrics_dict:
        problem_count += 1
        for metric_key in metrics:
            metric_value = dataset_metrics_dict[problem_name_key][metric_key]
            # print(f"for problem name {problem_name_key}, {metric_key} is: {metric_value}")
            if metric_key not in new_metrics_dict:
                new_metrics_dict[metric_key] = metric_value
            else:
                new_metrics_dict[metric_key] += metric_value

    # print('new_metrics_dict: ', new_metrics_dict)

    avgeraged_metrics_dict = {key : value / problem_count for key, value in new_metrics_dict.items()}
    # print("average_metrics_dict: ", avgeraged_metrics_dict)

    return avgeraged_metrics_dict
            


def setup_dataset(timestamp, problems_dir): # [TO DO]: this needs to be edited!!! for sure. actually i don't need this... 
    base_directory = Path(problems_dir)

    for problem in base_directory.iterdir():
        if problem.is_dir() and problem.name != 'metrics':
            outputs_path = problem / "outputs"
            stdouts_path = outputs_path / "stdouts"
            pseudocodes_path = outputs_path / "pseudocodes"
            results_path = outputs_path / "results"
            codes_path = outputs_path / "decoded_codes"
            metrics_path = outputs_path / "metrics"
            errors_path = outputs_path / "errors"

            outputs_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{outputs_path}' created successfully")
            stdouts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{stdouts_path}' created successfully")
            pseudocodes_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{pseudocodes_path}' created successfully")
            results_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{results_path}' created successfully")
            codes_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{codes_path}' created successfully")
            metrics_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{metrics_path}' created successfully")
            errors_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{metrics_path}' created successfully")
            
            ##### Make timestamps:
            pseudocodes_timestamp = pseudocodes_path / timestamp
            codes_timestamp = codes_path / timestamp
            metrics_timestamp = metrics_path / timestamp
            errors_timestamp = errors_path / timestamp

            pseudocodes_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{pseudocodes_timestamp}' created successfully")
            codes_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{codes_timestamp}' created successfully")
            metrics_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{metrics_timestamp}' created successfully")
            errors_timestamp.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
            print(f"Directory '{metrics_timestamp}' created successfully")

    overall_metrics_path = base_directory / "metrics"
    overall_metrics_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{overall_metrics_path}' created successfully")

def get_encoding_prompt(root_dir, generated_prompt, timestamp, stage, round):
    '''
    If the stage is 'decoder' then I need to load in a fixed encoder prompt. I should use the encoder prompt generated from this round.
    Check that the file is not empty though. It could be that I just wanted to run the decoding by itself. In which case run the initial
    default encoder prompt. If it's empty, I should raise an error if we're not in the first round.

    If the stage is 'encoder', then the encoding prompt is just the generated prompt.

    '''
    encoding_prompt = ''
    if stage == 'decoder':
        encoding_prompt_path = f"{root_dir}/outputs/prompts/{timestamp}/encoder_round_{round}.txt"

        encoding_file = Path(encoding_prompt_path)
        if encoding_file.is_file():
            with open(encoding_prompt_path, "r") as file: # [TO DO]: add a case for when i am just running decoding by itself.
                    encoding_prompt = file.read()
        else: # We are just doing the decoding by itself so need to load in default encoding prompt
            encoding_prompt_path = f"{root_dir}/prompts/common/initial_encoder_prompt.txt"
            with open(encoding_prompt_path, "r") as file:
                encoding_prompt = file.read()

    else:
        encoding_prompt = generated_prompt
    return encoding_prompt

def get_decoding_prompt(root_dir, generated_prompt, timestamp, stage, round):
    '''
    If the stage is 'encoder' then I need to load in a fixed decoder prompt. If it's the first round, then it needs to be the default 
    initial decoder prompt. If it's not the first round, then it needs to be the decoder prompt from the previous round.

    If the stage is 'decoder' then the decoding prompt is just the generated prompt
    '''
    decoding_prompt = ''
    assert round >= 0
    if stage == 'encoder':
        if round == 0: # load in default prompt
            decoding_prompt_path = f"{root_dir}/prompts/common/initial_decoder_prompt.txt"
            with open(decoding_prompt_path, "r") as file:
                decoding_prompt = file.read()
        else: # load in decoder prompt from previous round
            decoding_prompt_path = f"{root_dir}/outputs/prompts/{timestamp}/decoder_round_{round - 1}.txt"
            with open(decoding_prompt_path, "r") as file:
                decoding_prompt = file.read()
    else:
        decoding_prompt = generated_prompt

    return decoding_prompt

def run_dataset_scripting(timestamp, problems_dir, encoding_prompt, decoding_prompt):
    base_directory = Path(problems_dir)
    dataset_encoding_metrics = {}
    dataset_decoding_metrics = {}

    # problem_set = {"11_B", "20_A", "23_A", "26_A", "32_B", "32_C", "39_D", "41_C", "43_B", "55_A"}
    problem_set = {"11_B", "20_A", "23_A", "26_A", "32_B", "32_C", "39_D", "41_C",}


    for problem in base_directory.iterdir():
        # if problem.is_dir() and problem.name != "metrics" and problem.name != "18_B":
        if problem.is_dir() and problem.name != 'metrics':
            print("Problem: ", problem.name)
            dataset_encoding_metrics[problem.name] = {}
            dataset_decoding_metrics[problem.name] = {}
            llm_scripting_folder = problem / "llm_scripting"
            # outputs_folder = problem / "outputs"
            starter_code_path = llm_scripting_folder / "starter_code.py"
            # pseudocode_encoding_path = outputs_folder / "pseudocode_encoding.txt"
            final_decoding_path = llm_scripting_folder / "chat_generated_decoding.py"
            test_cases_folder = problem / "test_cases"
            # decoded_codes_path = outputs_folder / "decoded_codes" / timestamp

            
            num_test_cases = sum(1 for item in test_cases_folder.iterdir() if "input" in item.name) # need to get this somehow

            with open(str(starter_code_path), "r") as file:
                starter_code = file.read()

            encoding_metrics_dict = {}
            decoding_metrics_dict = {}
            avg_encoding_metrics_dict = {}
            avg_decoding_metrics_dict = {}
            metrics_dict = {}

            num_pseudocode_trials = 2
            num_decoding_trials = 3
             

            for pseudocode_num in range(num_pseudocode_trials): # we are doing 2 psuedocodes per problem
                # Encoding
                pseudocode_encoding = run_prompts([encoding_prompt], starter_code)
                # [TO DO]: develop a better system for where to print the pseudocodes to, or like i think i need to keep track of the iteration or else this will
                # be re-written over and over again, let's just exclude for now
                # pseudocode_path = outputs_folder / "pseudocodes" / timestamp /  f"pseudo_trial_{pseudocode_num+1}_pseudocode_encoding.txt"
                # pseudocode_path_name = str(pseudocode_path)

                # with open(pseudocode_path_name, "w") as file:
                #     file.write(pseudocode_encoding)

                max_num_test_cases_passed = 0
                optimal_decoding_code = ''

                for decoding_trial in range(num_decoding_trials): # we do these trials just in case there there are errors and we keep passing 0 test cases
                    final_decoding_response = run_prompts([decoding_prompt], pseudocode_encoding)
                    final_decoding_code = extract_code(final_decoding_response)

                    # [TO DO]: other than to run the code, i am not storing the decoded code, come back and check if that's how it's supposed to be

                    with open(str(final_decoding_path), "w") as file:
                        file.write(final_decoding_code)
            
                    num_test_cases_passed = run_test_cases(str(problem), problem.name, str(final_decoding_path), num_test_cases, 1, decoding_trial, timestamp)
                    if num_test_cases_passed > max_num_test_cases_passed:
                        max_num_test_cases_passed = num_test_cases_passed
                        optimal_decoding_code = final_decoding_code
                    if max_num_test_cases_passed == num_test_cases_passed:
                        actual_label = 1
                        break
                decoding_metrics_dict = get_metrics("code", optimal_decoding_code, starter_code, max_num_test_cases_passed, num_test_cases) 
                avg_decoding_metrics_dict = add_metrics(decoding_metrics_dict, avg_decoding_metrics_dict)
                

                encoding_metrics_dict = get_metrics("pseudocode", pseudocode_encoding, starter_code, max_num_test_cases_passed, num_test_cases) 
                avg_encoding_metrics_dict = add_metrics(encoding_metrics_dict, avg_encoding_metrics_dict)
            avg_decoding_metrics_dict = {key : value / (num_pseudocode_trials * num_decoding_trials) for key, value in avg_decoding_metrics_dict.items()}
            dataset_decoding_metrics[problem.name] = decoding_metrics_dict

            avg_encoding_metrics_dict = {key : value / num_pseudocode_trials for key, value in avg_encoding_metrics_dict.items()}
            dataset_encoding_metrics[problem.name] = avg_encoding_metrics_dict
                    
    return dataset_encoding_metrics, dataset_decoding_metrics

def calculate_metrics(dataset_encoding_metrics, dataset_decoding_metrics, stage, metrics_path):
    '''
    Reasoning for metrics weighting: // [TO DO]: this reasoning should be re-evaluated
    [TO DO]: choose better metrics
    
    1. line_count: should be as short as possible I think so to penalize long numbers the weight will be negative
    2. keyword_count: this should probably be high 
    3. comment_count: high count would improve performance but I don't want to rely on comments so will make this weight negative 
    4. avg_variable_name_length: should be on the higher end
    5. word_count: should not be too high
    '''
    metrics = {"line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "max_passing_rate"}
    metrics_weighting = {"line_count": -2, "keyword_count": 1, "comment_count": -1, "avg_variable_name_length": 1, "word_count": -2, "max_passing_rate": 10}
    # metrics = {'max_passing_rate'}
    # metrics_weighting = {"max_passing_rate": 1}

    # Step 1: standardize using linear normalizaion/Min-Max Normalization
    normalized_encoding_metrics = normalize_metrics(metrics, dataset_encoding_metrics)
    normalized_decoding_metrics = normalize_metrics(metrics, dataset_decoding_metrics)
    avg_encoding_metrics = average_metrics(metrics, normalized_encoding_metrics)
    avg_decoding_metrics = average_metrics(metrics, normalized_decoding_metrics)
    # avg_encoding_metrics = average_metrics(metrics, dataset_encoding_metrics)
    # avg_decoding_metrics = average_metrics(metrics, dataset_decoding_metrics)
    # if stage == 'encoder':
    #     print_metrics(normalized_encoding_metrics, avg_encoding_metrics, metrics_path)
    # else:
    #     print_metrics(normalized_decoding_metrics, avg_decoding_metrics, metrics_path)

    return avg_encoding_metrics, avg_decoding_metrics

    final_encoding_score = 0 
    final_decoding_score = avg_decoding_metrics["max_passing_rate"] * metrics_weighting["max_passing_rate"]
    final_encoding_score = avg_encoding_metrics["max_passing_rate"] * metrics_weighting["max_passing_rate"]

    # for metric in metrics:
    #     metric_weight = metrics_weighting[metric]
    #     print('metric weight: ', metric_weight)
    #     metric_avg_encoding_value = avg_encoding_metrics[metric]
    #     print('metric value: ', metric_avg_encoding_value)
    #     final_encoding_score += metric_avg_encoding_value * metric_weight
    #     print('addition to final score: ', metric_avg_encoding_value * metric_weight)
    #     metric_avg_decoding_value = avg_decoding_metrics[metric] # [TO DO]: what was i trying to do here?

    return final_encoding_score, final_decoding_score



def main():
    # Set logging level
    print("[*] Running ...")

    prompt_path = sys.argv[1]
    stage = sys.argv[2] # [TO DO]: pass in stage from reevo run_prompt function
    root_dir = sys.argv[3]  # [TO DO]: pass in root_dir from reevo run_prompt function
    round = int(sys.argv[4])
    timestamp = sys.argv[5]
    mood = sys.argv[6]
    assert mood in ['train', 'val']


    logging.info(f"Project Root: {root_dir}")

    problems_dir = f"{root_dir}/problems/10_short_problems" # [TO DO]: pass this in from main? or from reevo?
    metrics_path = f"{root_dir}/problems/10_short_problems/metrics"
    
    with open(prompt_path, 'r') as file:
        prompt = file.read()

    # now = datetime.now()
    # timestamp = f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}" # [TO DO]: pass in timestamp - done!
 
    encoding_prompt = get_encoding_prompt(root_dir, prompt, timestamp, stage, round)
    decoding_prompt = get_decoding_prompt(root_dir, prompt, timestamp, stage, round)
    if round == 0:
        setup_dataset(timestamp, problems_dir)
    dataset_encoding_metrics, dataset_decoding_metrics = run_dataset_scripting(timestamp, problems_dir, encoding_prompt, decoding_prompt)
    avg_encoding_metrics, avg_decoding_metrics = calculate_metrics(dataset_encoding_metrics, dataset_decoding_metrics, stage, metrics_path)
    if mood == 'train':
        print(f"[*] Final weighted score:")
        if stage == 'encoder':
            # print(final_encoding_score) # [TO DO]: eventually have a weighted score incorporating all the metrics, for now it will just be the passing rate
            print(avg_encoding_metrics['max_passing_rate'])
        else:
            print(avg_decoding_metrics['max_passing_rate'])

    else: # validation of best prompt
        save_metrics(avg_encoding_metrics, metrics_path, timestamp, stage, round)

if __name__ == "__main__":
    main()



