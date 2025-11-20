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
from utils.utils import init_client, file_to_string, set_up_dataset, preprocess_data, plot_pipeline
from evaluation.utils import evaluate_classifier_prompt, get_cosmetic_dataset, get_classifier_dataset, write_dataset_to_file, write_error_strings_to_file, evaluate_classifier_prompt_test
# from agents import GreedyRefine
from evaluation import Evaluator, get_data
from openai import OpenAI

from pipeline.autoencoder import AutoEncoder
from pipeline.cosmetic import Cosmetic
from pipeline.classifier import Classifier
from pipeline.experiment_runner import ExperimentRunner


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

    if cfg.algorithm == "reevo":
        from reevo import ReEvo as ga
    elif cfg.algorithm == "greedy":
        from agents.greedy_refine import GreedyRefine as ga
    elif cfg.algorithm == "direct_answer":
        from agents.direct_answer import DirectAnswer as ga
    else:
        raise NotImplementedError

    # uncomment below when first setting up
    # preprocess_data(ROOT_DIR) 
    
    # Main algorithm

    timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp

    # Run all 3 pipelines one after the other
    experiment_runner = ExperimentRunner(
        client=client, 
        src_dir=ROOT_DIR, 
        cfg=cfg,
        timestamp=timestamp,
        ga=ga,
    )

    experiment_runner.run_main_evolution()

    if (cfg.evolving_encoder or cfg.evolving_decoder or cfg.evolving_cosmetic or cfg.evolving_classifier) and not cfg.load_previous and cfg.use_timestamp: 
        set_up_dataset(timestamp, os.path.join(ROOT_DIR, "data", cfg.pipeline, cfg.dataset), cfg.num_iterations + 3) # plus 2 because of the final encoder and decoder verification at the end with train, val, and test splits


    if (cfg.evolving_encoder or cfg.evolving_decoder) and cfg.use_timestamp:
        encoding_agent = ga(
            client=client,
            src_dir=ROOT_DIR,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
            stage='encoder',
            previous_timestamp = '2025-09-18_21-00-18',
            prev_iter = 33
        )
        decoding_agent = ga(
            client=client,
            src_dir=ROOT_DIR,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
            stage='decoder',
            previous_timestamp = '2025-09-18_21-00-18',
            prev_iter = 34
        )

        data = get_data(cfg, os.path.join(ROOT_DIR, "data"), cfg.pipeline, cfg.split)

        evaluator = Evaluator(data, timeout=5) # [TO DO]: change timeout

        autoencoder = AutoEncoder(
            client=client, 
            src_dir=ROOT_DIR, 
            cfg=cfg,
            encoding_agent=encoding_agent, 
            decoding_agent=decoding_agent, 
            evaluator=evaluator,
            timestamp=timestamp,
            split=cfg.split,
            timeout=5, 
            model='gpt-4.1-mini', 
            stage='encoder', 
            
        )
        autoencoder.run()
        autoencoder.finalize()

    ######################## Run the cosmetic pipeline ################################

    '''
    To run the classifier, we need to create the pseudocode dataset. The following is the process:
    ok wait so what's the process? i have to run the cosmetic pipeline for the training and test versions right? ok so what
    are the steps:
    1. run autoencoder on the training set to generate the pseudocodes with their labels
        - each run will have its own timestamp
        - in config.yaml file, set the following variables:
        - dataset: leet_code # options: human_eval, leet_code
        - autoencoder_version: v0.3.0 # for leet_code dataset, specify which version you are using. default is v0.3.0
        - split: train # options: train or test
        - the end result is a folder named by the timestamp with all the pseudocodes and codes generated per iteration
    2. call get_cosmetic_dataset() to get AutoEncoderLabels_timestamp-train.jsonl
    3. run autoencoder on the testing set to generate the pseudocodes with their labels
    4. call get_cosmetic_dataset() to get AutoEncoderLabels_timestamp-test.jsonl
    5. run cosmetic pipeline on AutoEncoderLabels_timestamp-train.jsonl
    6. call get_classifier_dataset() passing with autoencoder and cosmetic timestamps set in cfg to create {dataset}Pseudocodes-v0.{version}.0-train.jsonl
    7. run cosmetic pipeline on AutoEncoderLabels_timestamp-test.jsonl
    8. call get_classifier_dataset() passing with autoencoder and cosmetic timestamps set in cfg to create {dataset}Pseudocodes-v0.{version}.0-test.jsonl
    9. run classifier pipeline


    '''

    if cfg.evolving_cosmetic:
        cosmetic_agent = ga(
            client=client,
            src_dir=ROOT_DIR,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
            stage='cosmetic'
        )

        get_cosmetic_dataset(cfg, ROOT_DIR)
        data = get_data(cfg, os.path.join(ROOT_DIR, "data"), cfg.pipeline, cfg.split)
        evaluator_cosmetic = Evaluator(data, timeout=5) 

        cosmetic = Cosmetic(
            client=client, 
            src_dir=ROOT_DIR, 
            cfg=cfg,
            agent=cosmetic_agent, 
            evaluator=evaluator_cosmetic,
            timestamp=timestamp,
            split=cfg.split,
            timeout=5, 
            model='gpt-4.1-mini',         
        )

        cosmetic.run()
    ######################## Run the classifier: ####################################################

    if cfg.evolving_classifier:
        classifier_agent = ga(
            client=client,
            src_dir=ROOT_DIR,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM ap
            stage='classifier',
        )

        get_classifier_dataset(cfg, ROOT_DIR, split='train', limit=150)
        get_classifier_dataset(cfg, ROOT_DIR, split='test', limit=150)
        data = get_data(cfg, os.path.join(ROOT_DIR, "data"), cfg.pipeline, cfg.split)
        evaluator_classifier = Evaluator(data, timeout=5) 

        classifier = Classifier(
            client=client, 
            src_dir=ROOT_DIR, 
            cfg=cfg,
            agent=classifier_agent, 
            evaluator=evaluator_classifier,
            timestamp=timestamp,
            split=cfg.split,
            timeout=5, 
            model='gpt-4.1-mini',         
        )

        classifier.run()
        classifier.finalize()

    ################################### Plotting: ##########################################################

    if cfg.plotting_pipeline:
        autoencoder_timestamp = '2025-11-18_14-39-59'
        classifier_timestamp = '2025-11-18_19-27-00'
        if not cfg.use_timestamp:
            autoencoder_timestamp = timestamp
            classifier_timestamp = timestamp
        plot_pipeline(cfg, ROOT_DIR, autoencoder_timestamp, "autoencoder")
        plot_pipeline(cfg, ROOT_DIR, classifier_timestamp, "classifier")
        plt.show()

    #######################################################
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
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')

    table_data = []
    for metric in metrics:
        table_data.append([metric, f"{leetcode_data[metric]:.3f}", f"{humaneval_data[metric]:.3f}"])

    table = ax.table(cellText=table_data,
                    colLabels=['Metric', 'LeetCode', 'HumanEval'],
                    cellLoc='center',
                    loc='center',
                    colColours=['#f0f0f0', '#d0e5ff', '#ffe5cc'])

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    plt.title('Metric Values Comparison', fontsize=14)
    plt.show()

    ######## BELOW is other stuff I tried but the main stuff is above: ###############

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