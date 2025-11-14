import hydra
import logging 
import os
from pathlib import Path
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import cProfile
import pstats
import traceback
from utils.utils import init_client, file_to_string, setup_dataset, minify_code
from evaluation.utils import save_metrics, save_prompt, get_pseudocode_dataset, evaluate_classifier_prompt, save_classifier_score, record_previous_best_solution, get_avg_test_case_length, get_num_difficulty, copy_difficulty_problems, get_cosmetic_dataset, get_classifier_dataset, write_dataset_to_file, write_error_strings_to_file, reformat_human_eval_file, print_feedback_from_file, evaluate_classifier_prompt_test, write_classifier_pseudocodes_to_file, organize_pseudocode, get_intersection_of_pseudocodes
# from agents import GreedyRefine
from evaluation import Evaluator, get_data
from openai import OpenAI

from pipeline.autoencoder import AutoEncoder
from pipeline.cosmetic import Cosmetic
from pipeline.classifier import Classifier


ROOT_DIR = os.getcwd()
logging.basicConfig(level=logging.INFO)

def run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round):
    # Write file to outputs/prompts directory so that next stage can load in the file
    best_prompt_path = f"{ROOT_DIR}/outputs/prompts/{timestamp}/{stage}_round_{round}.txt"
    with open(best_prompt_path, 'w') as file: 
        file.writelines(best_prompt_overall + '\n')
    # Run validation and redirect stdout to a file "best_code_overall_stdout.txt"
    with open(f"{ROOT_DIR}/problems/{problems_dir_name}/gpt_{stage}.txt", 'w') as file: #[TO DO]: not sure what this is for
        file.writelines(best_prompt_overall + '\n')
    test_script = f"{ROOT_DIR}/problems/eval_prompt.py" # instead, the eval script will compare the outputs
    # to the correct intputs and print out how many of the tests were passed
    test_script_stdout = "best_code_overall_val_stdout.txt"
    logging.info(f"Running validation script...: {test_script}")
    with open(test_script_stdout, 'w') as stdout:
        subprocess.run(["python", test_script, best_prompt_path, stage, ROOT_DIR, f'{round}', timestamp, 'val'], stdout=stdout)
    logging.info(f"Validation script finished. Results are saved in {test_script_stdout}.")

    # Print the results
    with open(test_script_stdout, 'r') as file:
        for line in file.readlines():
            logging.info(line.strip())

@hydra.main(version_base=None, config_path="cfg", config_name="config")
def main(cfg):
    workspace_dir = Path.cwd()
    # Set logging level
    logging.info(f"Workspace: {workspace_dir}")
    logging.info(f"Project Root: {ROOT_DIR}")
    # logging.info(f"Using LLM: {cfg.get('model', cfg.llm_client.model)}")
    logging.info(f"Using LLM: {cfg.llm_client.model}")
    logging.info(f"Using Algorithm: {cfg.algorithm}")

    client = init_client(cfg)

    print('client: ', client)

    if cfg.algorithm == "reevo":
        from reevo import ReEvo as ga
    elif cfg.algorithm == "greedy":
        from agents.greedy_refine import GreedyRefine as ga
    elif cfg.algorithm == "direct_answer":
        from agents.direct_answer import DirectAnswer as ga
#         agent = GreedyRefine(
#         timeout=10,
#         model='openai/o3-mini', # We use LiteLLM to call API
# )
    else:
        raise NotImplementedError
    
    # Main algorithm
    # problems_dir_name = 'human_eval'
    problems_dir_name = 'leet_code'
    # problems_dir_name = 'cosmetic_pseudocodes'
    # problems_dir_name = 'classifier_pseudocodes'
    if problems_dir_name == 'leet_code':
        # version = 'v0.1.0'
        version = 'v0.3.0-hard'
        # version = 'v3rd100'
        # version = 'v0.3.0tiny'
        split = 'train'
        # problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        problems_filename = f'LeetCodeDataset-{version}-{split}.jsonl'
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')
    elif problems_dir_name == "cosmetic_pseudocodes":
        # previous_timestamp = '2025-09-18_21-00-18'
        # previous_timestamp = '2025-09-18_04-55-13'
        # previous_timestamp = '2025-09-24_15-05-02'
        # previous_timestamp = '2025-09-25_22-10-58'
        previous_timestamp = '2025-09-26_19-55-20'
        # problems_filename = f"positive_labels_{previous_timestamp}.jsonl"
        problems_filename = f"pseudocode_labels_{previous_timestamp}.jsonl"
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')
    elif problems_dir_name == "classifier_pseudocodes":
        version = 1
        # problems_filename = f"LeetCode-pseudo-v0.{version}.0-train.jsonl"
        problems_filename = f"HumanEval-pseudo-v0.{version}.0-train.jsonl"
        # train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        # dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')
    else:
        split = "test"
        problems_filename = f'HumanEval-{split}.jsonl'
        data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')


    starting_iteration = cfg.starting_iteration
    iterations = cgf.num_iterations
    rounds = cfg.rounds

    # starting_iteration = 1
    # iterations = 32
    # rounds = 2
    timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp
    

    load_previous = False
    if load_previous:
        timestamp = '2025-09-13_12-15-28'
    
    evolving_encoding = False # depends on whether we are continuing in the encoding or decoding
    evolving_decoding = False # This should start off as False always
    evolving_cosmetic = False
    evolving_classifier = False

    # if (evolving_encoding or evolving_decoding or evolving_cosmetic or evolving_classifier) and not load_previous: 
    #     setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 2) # plus 2 because of the final encoder and decoder verification at the end
    setup_dataset(timestamp, f"{ROOT_DIR}/data/{cfg.pipeline}/{cfg.dataset}", iterations + 3) # plus 2 because of the final encoder and decoder verification at the end with train, val, and test splits

    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}") # [TO DO]: decide if i still need this
    generated_prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    metrics_path = f"{ROOT_DIR}/data/{problems_dir_name}/metrics"


        # previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{iteration}", "previous_best", previous_best.json)
    # print(f"Directory '{generated_prompts_path}' created successfully")
    # print('prompt path: ', str(generated_prompts_path))

    encoding_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='encoder'
    )
    decoding_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='decoder'
    )

    prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_decoder_prompt.txt")
    prev_encoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_encoder_prompt.txt")

    if load_previous and (evolving_encoding or evolving_decoding):
        # if starting_iteration % 8 <= 4: # encoding stage
        #     encoding_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{starting_iteration - 1}", "previous_best", "previous_best.json")
        # else:
        prev_encoder_iter = 9 # [TO DO]: CHANGE
        encoding_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_encoder_iter}", "previous_best", "previous_best.json")
        encoding_agent.load_previous(encoding_previous_best_path) # [TO DO]: write load_previous() function
        # prev_decoder_iter = 0
        # prev_decoder_filename = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_decoder_iter}", "prompts", "decoder_stage_decoding_prompt.txt")
        # prev_decoder_prompt = file_to_string(prev_decoder_filename)
        if starting_iteration >= (rounds + 2):
            # if starting_iteration % 8 > 4:
            prev_decoder_iter = 8 # [TO DO]: CHANGE
            decoding_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_decoder_iter}", "previous_best", "previous_best.json")
            decoding_agent.load_previous(decoding_previous_best_path)
            prev_encoder_prompt = encoding_agent.finalize()
            # prev_encoder_iter = 0
            # prev_encoder_filename = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_encoder_iter}", "prompts", "encoder_stage_encoding_prompt.txt")
            # prev_encoder_prompt = file_to_string(prev_encoder_filename)
        if starting_iteration >= (2*rounds + 1): # After at least one round of decoding 
            prev_decoder_prompt = decoding_agent.finalize()
        
    if load_previous and evolving_cosmetic:
        prev_cosmetic_iter = 0 

    evaluator = Evaluator(data, timeout=5) # [TO DO]: change timeout

    autoencoder = AutoEncoder(
        client=client, 
        src_dir=ROOT_DIR, 
        cfg=cfg,
        encoding_agent=encoding_agent, 
        decoding_agent=decoding_agent, 
        evaluator=evaluator,
        timeout=5, 
        model='gpt-4.1-mini', 
        stage='encoder', 
        timestamp=timestamp
    )

    autoencoder.run()
    autoencoder.finalize()


    ######################## Store pseudocode in a pandas dataframe: ################################
    problems_dir = f"{ROOT_DIR}/data/{problems_dir_name}"
    # avg_test_case_num = get_avg_test_case_length(os.path.join(problems_dir, problems_filename))
    # print("avg num of test cases: ", avg_test_case_num)
    start = 1
    end = 3000
    difficulty = "Hard"
    # for v0.3.0 in first 800, there is 165 Hard, 444 Medium, and 190 Easy
    # in next 800, 801 through 1600, there is 177 Hard, 416 Medium, and 208 Easy
    # ok in total there are ony 532 Hard...
    # for v0.3.0 test, there are 108 Hard and 188 Medium. ok let's try to do a 50/50 split
    # new_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
    # num_difficulty_problems = get_num_difficulty(os.path.join(problems_dir, new_filename), difficulty, start, end)
    # print(f"number of problems with difficulty {difficulty} is: ", num_difficulty_problems)
    # Get hard pseudocodes
    difficulty_map = {"Hard": 100, "Medium": 100}
    limit = 200
    problems_filename = f'LeetCodeDataset-v0.3.0-test.jsonl'
    new_filename = f'LeetCodeDataset-v0.3.0-hard-test.jsonl'
    # copy_difficulty_problems(os.path.join(problems_dir, problems_filename), os.path.join(problems_dir, new_filename), difficulty_map, limit)

    ######################## Create cosmetic changes for the positive labels: ################################

    if load_previous and evolving_cosmetic:
        prev_iter = 0
        cosmetic_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_iter}", "previous_best", "previous_best.json")
        cosmetic_agent.load_previous(cosmetic_previous_best_path)

    evaluator_cosmetic = Evaluator(data, timeout=5) 

    cosmetic_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='cosmetic'
    )

    if cfg.evolving_cosmetic:
        get_cosmetic_dataset(cfg)

        cosmetic = Cosmetic(
            client=client, 
            src_dir=ROOT_DIR, 
            cfg=cfg,
            agent=cosmetic_agent, 
            evaluator=evaluator_cosmetic,
            timestamp=timestamp,
            final_iter=34,
            previous_timestamp='2025-09-18_21-00-18',
            timeout=5, 
            model='gpt-4.1-mini',         
        )

        cosmetic.run()
    ######################## Run the classifier: ####################################################

    version = 1
    problems_filename = f"HumanEval-pseudo-v0.{version}.0-train.jsonl"
    # train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
    # dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
    train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-train.jsonl" )
    dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-dev.jsonl")
    classifier_dataset_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes")
    
    classifier_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='classifier'
    )
    
    if cfg.evolving_classifier:
        get_classifier_dataset(cfg, limit=150)

        classifier = Classifier(
            client=client, 
            src_dir=ROOT_DIR, 
            cfg=cfg,
            agent=classifier_agent, 
            evaluator=evaluator_classifier,
            timestamp=timestamp,
            final_iter=34,
            previous_timestamp='2025-09-18_21-00-18',
            timeout=5, 
            model='gpt-4.1-mini',         
        )

        classifier.run()
        classifier.finalize()

    # Plot:
    # Load results
    # problems_dir_path = Path(f"{ROOT_DIR}/data/{problems_dir_name}")
    # problems = [problem.name for problem in problems_dir_path.iterdir() if (problem.is_dir() and problem.name != 'metrics')]
    # metrics = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "max_passing_rate"]
    # metrics = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "passing_rate", "avg_score"]
    # metrics = ["line_count", "passing_rate", "avg_score"]
   
    problems = ["HumanEval/0", "HumanEval/1", "HumanEval/2", "HumanEval/3", "HumanEval/4"]
    problems = ["two-sum", "add-two-numbers", "longest-substring-without-repeating-characters", "median-of-two-sorted-arrays", "zigzag-conversion"]
    # problems = ["32_C", "39_D", "41_C", "43_B", "55_A"]
    metrics = ["avg_score", "passing_rate"]
    metrics = ["line_count", "keyword_count", "comment_count", "avg_syllables_per_word", "word_count", "line_length", "avg_word_length", "syllable_count", "readability", "avg_words_per_line", "passing_rate"]
    # metrics = ["avg_score"]
    # metrics = ["passing_rate"]
    # metrics = ['readability']
    # metrics.extend(problems)
    # print('metrics: ', metrics)
    # metrics = ["line_count"]
    # timestamp = '2025-06-19_14-18-09'
    # timestamp = '2025-06-16_14-15-27'
    # timestamp = '2025-06-19_17-37-11'

    # timestamp = '2025-09-15_01-29-56' # readability: "avg_syllables_per_word", "line_count"]
    timestamp = '2025-09-18_04-55-13'
    # timestamp = '2025-09-18_21-00-18'
    # timestamp = '2025-09-24_15-05-02'
    # timestamp = '2025-09-25_13-37-25'
    # timestamp = '2025-09-25_14-14-02'
    # timestamp = '2025-09-25_15-00-26'
    # timestamp = '2025-09-25_15-41-49'
    # timestamp = '2025-09-25_17-46-20'
    # timestamp = '2025-09-25_18-36-13'
    # timestamp = '2025-09-26_15-07-49'

    # DirectAnswer:
    timestamp = '2025-09-26_19-55-20' # 0.3.0-hard-test
    problems_dir_name = 'leet_code'
    problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    with open(problem_metrics_file, "r") as f:
        data = json.load(f)
    df_enc_2 = pd.DataFrame(data)

    # metrics = ["passing_rate", "avg_word_length", "avg_words_per_line"]
    # metrics = ["passing_rate", "avg_syllables_per_word", "avg_words_per_line"]
    # metrics = ["passing_rate"]
    # metrics = ["accuracy_score", "true_positive", "true_negative", "near_miss", "cosmetic"]
    # metrics = ["passing_rate", "avg_word_length"]
    # metrics = ["avg_score"]
    # title="Metrics Over Time - Autoencoder - HumanEval"
    # plt.figure(2)  # Use a different figure number

    # Exclude the last row to not put the test score ther as well
    # df_filtered = df_enc_2.iloc[1:]
    df_filtered = df_enc_2

    # Filter for encoder stages only
    encoder_data = df_filtered[df_filtered['stage'] == 'encoder']

    # df_filtered = df_enc_2.iloc[:-1]
    ax2 = encoder_data.plot(
        x="iter",              # X-axis
        y=metrics,                         # Y-columns (as a list)
        figsize=(10, 5),                   # Figure size
        title="Autoencoder Scores - LeetCode",  # Plot title
        grid=True,                         # Show grid
        marker="o"                         # Marker style
    )

    plt.tight_layout()
    # plt.savefig(f"{ROOT_DIR}/outputs/thesis_draft/classifier_{timestamp}.png", bbox_inches='tight', dpi=300)
    plt.show()
    ###########################################

    categories = ['Datasets', 'Agent Frameworks']
    categories = ['GreedyRefine', 'DirectAnswer']

    # This is the dataset figure
    # Data for the visualization
    datasets = ['GreedyRefine', 'DirectAnswer']
    metrics = ['avg_score', 'avg_passing_rate', 'avg_syllables_per_word', 
            'classifier_score_train', 'classifier_score_val', 'classifier_score_test']
    # metrics = ['avg_score', 'avg_passing_rate', 'avg_word_length']

    # leetcode_data = {
    #     'avg_score': 1.949,
    #     'avg_passing_rate': 0.885,
    #     'avg_syllables_per_word': 0.266,
    #     'classifier_score_train': 0.677,
    #     'classifier_score_test': 0.59
    # }

    # humaneval_data = {
    #     'avg_score': 2.012,
    #     'avg_passing_rate': 0.895,
    #     'avg_syllables_per_word': 0.279,
    #     'classifier_score_train': 0.435,
    #     'classifier_score_test': 0.52
    # }
    leetcode_data = {
        'avg_score': 1.949,
        'avg_passing_rate': 0.885,
        'avg_syllables_per_word': 0.266,
        'classifier_score_train': 0.677,
        'classifier_score_val': 0.729,
        'classifier_score_test': 0.59
    }

    humaneval_data = {
        'avg_score': 1.778,
        'avg_passing_rate': 0.888,
        'avg_syllables_per_word': 0.223,
        'classifier_score_train': 0.500,
        'classifier_score_val': 0.543,
        'classifier_score_test': 0.547
    }

    
    leetcode_values = [leetcode_data[metric] for metric in metrics] # Convert to arrays for easier plotting
    humaneval_values = [humaneval_data[metric] for metric in metrics]

    fig, ax2 = plt.subplots(figsize=(16, 8))
    # fig.suptitle('Performance Comparison: LeetCode vs HumanEval', fontsize=16, fontweight='bold')
    fig.suptitle('Performance Comparison: GreedyRefine vs DirectAnswer for avg_word_length', fontsize=16, fontweight='bold')

    # Second subplot: Grouped bar chart for detailed comparison
    x = np.arange(len(metrics))
    width = 0.35

    bars1 = ax2.bar(x - width/2, leetcode_values, width, label='GreedyRefine', color='#1f77b4', alpha=0.8)
    bars2 = ax2.bar(x + width/2, humaneval_values, width, label='DirectAnswer', color='#ff7f0e', alpha=0.8)

    ax2.set_xlabel('Metrics')
    ax2.set_ylabel('Values')
    # ax2.set_title('Detailed Metric Comparison')
    ax2.set_xticks(x)
    ax2.set_xticklabels(metrics, rotation=45, ha='right')
    ax2.legend()

    # Add value labels on bars
    def add_value_labels(bars, ax):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    add_value_labels(bars1, ax2)
    add_value_labels(bars2, ax2)

    plt.tight_layout()
    plt.savefig(f"{ROOT_DIR}/outputs/thesis_draft/agent_frameworks_avg_syllables_per_word.png", bbox_inches='tight', dpi=300)
    plt.show()

    # Additional visualization: Side-by-side metrics table
    # fig, ax = plt.subplots(figsize=(12, 4))
    # ax.axis('tight')
    # ax.axis('off')

    # table_data = []
    # for metric in metrics:
    #     table_data.append([metric, f"{leetcode_data[metric]:.3f}", f"{humaneval_data[metric]:.3f}"])

    # table = ax.table(cellText=table_data,
    #                 colLabels=['Metric', 'LeetCode', 'HumanEval'],
    #                 cellLoc='center',
    #                 loc='center',
    #                 colColours=['#f0f0f0', '#d0e5ff', '#ffe5cc'])

    # table.auto_set_font_size(False)
    # table.set_fontsize(10)
    # table.scale(1, 1.5)

    # plt.title('Metric Values Comparison', fontsize=14)
    # plt.show()

    # filtered_df_2 = df_enc_2[df_enc_2['stage'] == 'encoder']
    # max_index = filtered_df_2['avg_score'].idxmax()
    # max_row = filtered_df_2.loc[max_index]

    # print("for avg_word_length, avg_words_per_line :")
    # print(f"Highest avg_score: {max_row['avg_score']}")
    # print(f"Found at iteration: {max_row['iter']}")
    # print(f"Full row data:\n{max_row}")
    # print('\n')

    # plt.show()


    # classifier_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_classifier_metrics.json"
    # with open(classifier_metrics_file, "r") as f:
    #     classifier_data = json.load(f)

    # decoding_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_decoder_metrics.json"
    # with open(decoding_metrics_file, "r") as f:
    #     decoding_data = json.load(f)

    #### Encoding Metrics
    # timestamp = '2025-09-11_22-54-06' # readability: "avg_word_length", "avg_words_per_line"
    # timestamp = '2025-09-11_11-17-39' # readability: "avg_word_length", "line_count"
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc = pd.DataFrame(data)

    # # plt.figure(1)
    # # df.plot(x="round", y="max_passing_rate")

    # metrics = ["passing_rate", "avg_word_length", "line_count"]

    # # Create the second plot with metrics
    # plt.figure(1)  # Use a different figure number
    # ax1 = df_enc.plot(
    #     x="iter",              # X-axis
    #     y=metrics,                         # Y-columns (as a list)
    #     figsize=(10, 5),                   # Figure size
    #     title="Metrics Over Time - Encoding",  # Plot title
    #     grid=True,                         # Show grid
    #     marker="o"                         # Marker style
    # )

    # filtered_df = df_enc[df_enc['stage'] == 'encoder']
    # max_index = filtered_df['avg_score'].idxmax()
    # max_row = filtered_df.loc[max_index]

    # print("for avg_word_length :")
    # print(f"Highest avg_score: {max_row['avg_score']}")
    # print(f"Found at iteration: {max_row['iter']}")
    # print(f"Full row data:\n{max_row}")
    # print('\n')

    # timestamp = '2025-09-12_11-31-03' # readability: "avg_syllables_per_word", "avg_words_per_line"]
    # timestamp = '2025-09-10_19-53-08' # readability: "avg_syllables_per_word", "line_count"]
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc_2 = pd.DataFrame(data)

    # metrics = ["passing_rate", "avg_syllables_per_word", "line_count"]

    # plt.figure(2)  # Use a different figure number
    # ax2 = df_enc_2.plot(
    #     x="iter",              # X-axis
    #     y=metrics,                         # Y-columns (as a list)
    #     figsize=(10, 5),                   # Figure size
    #     title="Metrics Over Time - Encoding",  # Plot title
    #     grid=True,                         # Show grid
    #     marker="o"                         # Marker style
    # )

    # filtered_df_2 = df_enc_2[df_enc_2['stage'] == 'encoder']
    # max_index = filtered_df_2['avg_score'].idxmax()
    # max_row = filtered_df_2.loc[max_index]

    # print("for avg_syllables_per_word :")
    # print(f"Highest avg_score: {max_row['avg_score']}")
    # print(f"Found at iteration: {max_row['iter']}")
    # print(f"Full row data:\n{max_row}")
    # print('\n')

    # plt.show()

    # df_enc = pd.DataFrame(encoding_data)
    # df.plot(x="round", y="max_passing_rate")
    # plt.figure(1)
    # ax1 = df_enc.plot(
    #     x="iteration-rounds",                      # X-axis
    #     y=metrics,  # Y-columns (as a list)
    #     figsize=(10, 5),               # Figure size
    #     title="Metrics Over Time - Encoding",     # Plot title
    #     grid=True,                     # Show grid
    #     marker="o"                     # Add markers (optional)
    # )

    # # Customize the plot
    # ax1.set_xlabel("Iteration-Rounds")
    # ax1.set_ylabel("Value")
    # plt.legend(title="Metrics")        # Show legend with a title
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_encoder_metrics.png")
    # timestamp = '2025-09-06_13-14-33'
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc = pd.DataFrame(data)

    # def create_metric_figure(metrics_subset, fig_title):
    #     """Helper function to create a figure for a subset of metrics"""
    
    # for ax, metric in zip(axes, metrics_subset):

    # fig1, axes = plt.subplots(5, 1, figsize=(20, 16), sharex=True)
    # axes = axes.flatten()


    # for ax, problem in zip(axes, problems):
    #     for i in range(len(df_enc)-1): # First, plot the BASELINE_METRIC - avg score (in all subplots)
    #         color = 'gray'  # Distinct color for baseline
    #         alpha = 0.5  # Make it semi-transparent
    #         ax.plot(
    #             df_enc['iter'].iloc[i:i+2],
    #             df_enc['avg_score'].iloc[i:i+2],
    #             color=color,
    #             linestyle=':',
    #             alpha=alpha,
    #             marker='d'  # Diamond marker for baseline
    #         )
        # Second, plot the BASELINE_METRIC - passing rate (in all subplots)
        # for i in range(len(df_enc)-1):
        #     color = 'purple'  # Distinct color for baseline
        #     alpha = 0.5  # Make it semi-transparent
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc['passing_rate'].iloc[i:i+2],
        #         color=color,
        #         linestyle='--',
        #         alpha=alpha,
        #         marker='x'  # Diamond marker for baseline
        #     )

        # Next, plot each problem metric in its own subplot
        # for i in range(len(df_enc)-1):
        #     color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
        #     marker = 'o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
            
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc[problem+"_avg_syllables_per_word"].iloc[i:i+2],
        #         color + '-',
        #         marker=marker
        #     )
        
        # ax.set_title(problem)
        # ax.grid(True)

    # Add common legend
    # handles = [
    #     plt.Line2D([], [], color='gray', linestyle=':', marker='d', label='Avg Syllables per word'),
    #     # plt.Line2D([], [], color='purple', linestyle='--', marker='x', label='Passing Rate'),
    #     plt.Line2D([], [], color='b', marker='o', linestyle='-', label='Encoder'),
    #     plt.Line2D([], [], color='r', marker='s', linestyle='-', label='Decoder')
    # ]
    # fig1.legend(handles=handles, loc='lower center', ncol=2)

    # Fig 2:

    # fig2, axes = plt.subplots(5, 1, figsize=(20, 16), sharex=True)
    # axes = axes.flatten()


    # for ax, problem in zip(axes, problems):
        # First, plot the BASELINE_METRIC - avg score (in all subplots)
        # for i in range(len(df_enc)-1):
        #     color = 'gray'  # Distinct color for baseline
        #     alpha = 0.5  # Make it semi-transparent
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc['avg_score'].iloc[i:i+2],
        #         color=color,
        #         linestyle=':',
        #         alpha=alpha,
        #         marker='d'  # Diamond marker for baseline
        #     )
        # Second, plot the BASELINE_METRIC - passing rate (in all subplots)
        # for i in range(len(df_enc)-1):
        #     color = 'purple'  # Distinct color for baseline
        #     alpha = 0.5  # Make it semi-transparent
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc['passing_rate'].iloc[i:i+2],
        #         color=color,
        #         linestyle='--',
        #         alpha=alpha,
        #         marker='x'  # Diamond marker for baseline
        #     )

        # Next, plot each problem metric in its own subplot
        # for i in range(len(df_enc)-1):
        #     color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
        #     marker = 'o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
            
        #     ax.plot(
        #         df_enc['iter'].iloc[i:i+2],
        #         df_enc[problem+f"_passing_rate"].iloc[i:i+2],
        #         color + '-',
        #         marker=marker
        #     )
        
        # ax.set_title(problem)
        # ax.grid(True)

    # Add common legend
    # handles = [
    #     # plt.Line2D([], [], color='gray', linestyle=':', marker='d', label='Avg Score'),
    #     plt.Line2D([], [], color='purple', linestyle='--', marker='x', label='Passing Rate'),
    #     plt.Line2D([], [], color='b', marker='o', linestyle='-', label='Encoder'),
    #     plt.Line2D([], [], color='r', marker='s', linestyle='-', label='Decoder')
    # ]
    # fig2.legend(handles=handles, loc='lower center', ncol=2)

    # fig1.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_avg_syllables_per_word.png", bbox_inches='tight', dpi=300)
    # fig2.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_passing_rate.png", bbox_inches='tight', dpi=300)

    # plt.tight_layout()
    # plt.show()
    ##########
    # problem = '41_C'
    # problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    # with open(problem_metrics_file, "r") as f:
    #     data = json.load(f)
    # df_enc = pd.DataFrame(data)

    # colors = ['b' if df_enc['stage'].iloc[i] == 'encoder' else 'r' for i in range(len(df_enc))]
    # markers = ['o' if df_enc['stage'].iloc[i] == 'encoder' else 's' for i in range(len(df_enc))]
    # passing_rates = [df_enc[problem].iloc[i] for i in range(len(df_enc))]
    # iters = [df_enc['iter'].iloc[i] for i in range(len(df_enc))]
    # print('passing_rates:', passing_rates)
    # print('iters:', iters)

    # for i in range(len(df_enc)-1):
    #     color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
    #     plt.plot(
    #         df_enc['iter'].iloc[i:i+2],
    #         df_enc[problem].iloc[i:i+2], # passing rate for this specific problem
    #         color + '-',
    #         marker='o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
    #     )
    # for x, y, color, marker in zip(iters, passing_rates, colors, markers):
    #     plt.scatter(x, y, c=color, marker=marker, s=100)

    # # Connect points with a line (optional)
    # plt.plot(iters, passing_rates, 'k-', alpha=0.3)  # gray connecting line

    # # Create custom legend
    # import matplotlib.lines as mlines
    # blue_line = mlines.Line2D([], [], color='blue', marker='o', linestyle='-', label='Encoder')
    # red_line = mlines.Line2D([], [], color='red', marker='s', linestyle='-', label='Decoder')
    # plt.legend(handles=[blue_line, red_line])

    # # Add labels and title
    # plt.xlabel('Number of Iterations')
    # plt.ylabel('Passing Rate')
    # plt.title('Passing Rate by Stage Across Iterations')
    # plt.grid(True)

    # # Show the plot
    # plt.show()

    ### Decoding Metrics
    # df_dec = pd.DataFrame(decoding_data)
    # # df.plot(x="round", y="max_passing_rate")
    # plt.figure(2)
    # ax2 = df_dec.plot(
    #     x="iteration-rounds",                      # X-axis
    #     y=metrics,  # Y-columns (as a list)
    #     figsize=(10, 5),               # Figure size
    #     title="Metrics Over Time - Decoding",     # Plot title
    #     grid=True,                     # Show grid
    #     marker="o"                     # Add markers (optional)
    # )

    # Customize the plot
    # ax2.set_xlabel("Iteration-Rounds")
    # ax2.set_ylabel("Value")
    # plt.legend(title="Metrics")        # Show legend with a title
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_decoder_metrics.png")
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_encoder_decoder_metrics.png")


    ### Classifier Metrics
    # df_clas = pd.DataFrame(classifier_data)
    # # df.plot(x="round", y="max_passing_rate")
    # plt.figure(1)
    # ax1 = df_clas.plot(
    #     x="iter",                      # X-axis
    #     y=metrics,  # Y-columns (as a list)
    #     figsize=(10, 5),               # Figure size
    #     title="Score Over Time - Classifier",     # Plot title
    #     grid=True,                     # Show grid
    #     marker="o"                     # Add markers (optional)
    # )

    # # # Customize the plot
    # ax1.set_xlabel("Iterations")
    # ax1.set_ylabel("Value")
    # plt.legend(title="Score")        # Show legend with a title
    # plt.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_encoder_metrics.png")
    # plt.show()



if __name__ == "__main__":
    main()