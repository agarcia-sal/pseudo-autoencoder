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
from utils.utils import init_client, file_to_string, setup_dataset, minify_code
from evaluation.utils import save_metrics, save_prompt, get_pseudocode_dataset, evaluate_classifier_prompt, save_classifier_score
# from agents import GreedyRefine
from evaluation import Evaluator, get_data
from openai import OpenAI


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
        from agents.greedy_refine import GreedyRefine as ga # [TO DO]: change ga as agent; figure out how to blend the two
#         agent = GreedyRefine(
#         timeout=10,
#         model='openai/o3-mini', # We use LiteLLM to call API
# )
    else:
        raise NotImplementedError
    
    # Main algorithm
    problems_dir_name = '10_short_problems'
    iterations =  64# [TO DO]: CO-Bench paper uses 64
    rounds = 4# [TO DO]: this is a hyperparameter i need to tune; am using 10 for now
    timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp
    metrics_path = f"{ROOT_DIR}/data/{problems_dir_name}/metrics"
    # minify_code(f"{ROOT_DIR}/data/{problems_dir_name}")
    setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 2) # plus 2 because of the final encoder and decoder verification at the end
    

    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}")
    generated_prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    # print(f"Directory '{generated_prompts_path}' created successfully")
    # print('prompt path: ', str(generated_prompts_path))

    evolving_encoding = True
    evolving_decoding = False # This should start off as False always

    # client = OpenAI(
    #     # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    #     api_key = os.getenv('OPENAI_API_KEY'),
    # )

    data = get_data(problems_dir_name, src_dir=f'{ROOT_DIR}/data')

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
    evaluator = Evaluator(data, timeout=10) # [TO DO]: change timeout

    prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_decoder_prompt.txt")
    prev_encoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_encoder_prompt.txt")

    # profiler = cProfile.Profile()
    # profiler.enable()

    # Run for 20/64 iterations
    for it in range(1, iterations + 1):
        # Encoding:
        # print(f'iteration: {it}')
        if evolving_encoding:
            stage = 'encoder'
            try: # may hit an LLM rate limite
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                # for round in range(rounds):
                print('right before calling agent.step()')
                prompt = encoding_agent.step()
                print('right after calling agent.step()')
                # print('prompt from agent.step() looks like: ', prompt)
                if prompt is None:  # agent decides to terminate
                    # print('prompt is none')
                    break
                print('right before calling evaluate()')
                feedback = evaluator.evaluate(prompt, prev_decoder_prompt, stage, timestamp, it, client)  # Run evaluation
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                # print('feedback: ', feedback)
                print('right before calling feedback() within the round')
                encoding_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                print('right after calling feedback() within the round')
                # Get the final solution
                print('right before calling finalize()')
                if it % rounds == 0: # about to switch over to the next stage
                    best_prompt_so_far = encoding_agent.finalize()
                    prev_encoder_prompt = best_prompt_so_far
                print('right after calling fnalize()')
                if feedback.dev_score == 1.0:
                    print('prompt: ')
                    print(prompt)
                    break
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round
        if evolving_decoding:
            stage = 'decoder'
            try:
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                # for round in range(rounds):
                # print('in decoding round:', round)
                prompt = decoding_agent.step()
                if prompt is None:  # agent decides to terminate
                    break # [TO DO]: or should this be 'continue'??
                feedback = evaluator.evaluate(prompt, prev_encoder_prompt, stage, timestamp, it, client)  # Run evaluation
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                # [TO DO]: add a try except or catch error when there is not an encoder prompt returned
                decoding_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                # Get the final solution
                # print('right before calline finalize()')
                if it % rounds == 0: # about to switch over to the next stage
                    best_prompt_so_far = decoding_agent.finalize()
                    prev_decoder_prompt = best_prompt_so_far

            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round
        if it % rounds == 0: # maybe start at iterations = 1 ? and put this at the bottom of the loop
            evolving_encoding = not evolving_encoding
            evolving_decoding = not evolving_decoding

    # Finalize:
    print('finalize section:')
    print('encoding:')
    prompt = encoding_agent.finalize()
    save_prompt(str(generated_prompts_path), prompt, iterations + 1, 'encoder')
    feedback = evaluator.evaluate(prompt, prev_decoder_prompt, 'encoder', timestamp, iterations + 1, client)
    avg_metrics = feedback.avg_metrics
    save_metrics(avg_metrics, metrics_path, timestamp, 'encoder', iterations + 1)
    # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics: [TO DO]!

    print('decoding:')
    prompt = decoding_agent.finalize()
    save_prompt(str(generated_prompts_path), prompt, iterations, 'decoder')
    feedback = evaluator.evaluate(prompt, prev_encoder_prompt, 'decoder', timestamp, iterations + 2, client)
    avg_metrics = feedback.avg_metrics
    save_metrics(avg_metrics, metrics_path, timestamp, 'decoder', iterations + 2)
    # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics [TO DO]!

    # print('best encoding prompt: ')
    # print(prev_encoder_prompt)
    # print('best decoder prompt:')
    # print(prev_decoder_prompt)

    ######################## Store pseudocode in a pandas dataframe: ################################
    store_pseudocode = False
    if store_pseudocode:
        stage = 'encoder'
        # timestamp = '2025-06-16_14-15-27'
        timestamp = '2025-06-19_17-37-11'
        json_path_name = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
        problems_dir = f"{ROOT_DIR}/data/{problems_dir_name}"
        positive_examples_list, negative_examples_list = get_pseudocode_dataset(json_path_name, problems_dir, timestamp, stage)

    ######################## Run the classifier: ####################################################
    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}")
    generated_prompts_path.mkdir(parents=True, exist_ok=True)

    classifier_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='classifier'
    )
    evolving_classifier = False
    classifier_iterations = 1
    rounds = 1

    for it in range(classifier_iterations):
        # Encoding:
        if evolving_classifier:
            stage = 'classifier'
            try: # may hit an LLM rate limite
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                for round in range(rounds):
                    # print('right before calling agent.step()')
                    prompt = classifier_agent.step()
                    # print('step:', 0)
                    # print('right after calling agent.step()')
                    # print('prompt from agent.step() looks like: ', prompt)
                    if prompt is None:  # agent decides to terminate
                        # print('prompt is none')
                        break
                    # print('right before calling evaluate() within the round')
                    score = evaluate_classifier_prompt(positive_examples_list, negative_examples_list, prompt, client)
                    # print('step:', 1)
                    feedback = evaluator.get_feedback_classifier(score)  # Run evaluation
                    # print('step:', 2)
                    # save_metrics(avg_metrics, metrics_path, timestamp, stage, it, round, rounds)
                    save_classifier_score(score, metrics_path, timestamp, stage, it, round, rounds)
                    # print('step:', 3)
                    save_prompt(str(generated_prompts_path), prompt, it, round, stage)
                    # print('step:', 4)
                    # print('feedback: ', feedback)
                    # print('right before calling feedback() within the round')
                    classifier_agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback
                    # print('step:', 5)
                    # print('right after calling feedback() within the round')
                # Get the final solution
                # print('right before calling finalize()')
                # print('right after calling save_metrics()')
                # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics: [TO DO]!
                # if feedback.dev_score == 1.0:
                #     print('prompt: ')
                #     print(prompt)
                #     break
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round
    # prompt = classifier_agent.finalize()
    # save_prompt(str(generated_prompts_path), prompt, classifier_iterations, round, stage)
    # # print('right before calling the final evaluate()')
    # score = evaluate_classifier_prompt(positive_examples_list, negative_examples_list, prompt, client)
    # feedback = evaluator.get_feedback_classifier(score)
    
    # print('avg_metrics: ', avg_metrics)
    # save_metrics(avg_metrics, metrics_path, timestamp, stage, it, rounds, rounds)
    # save_classifier_score(score, metrics_path, timestamp, stage, classifier_iterations, round, rounds)
    # print('pseudocode_dataset_list: ')
    # print(pseudocode_dataset_list)

    # profiler.disable()
    # profiler.print_stats(sort='time') 
    # profiler.dump_stats('profile_data.prof') 
    # stats = pstats.Stats('profile_data.prof')
    # stats.strip_dirs().sort_stats('time').print_stats(10)  # show top 10 by internal time          
    # Plot:
    # Load results
    # problems_dir_path = Path(f"{ROOT_DIR}/data/{problems_dir_name}")
    # problems = [problem.name for problem in problems_dir_path.iterdir() if (problem.is_dir() and problem.name != 'metrics')]
    # metrics = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "max_passing_rate"]
    # metrics = ["line_count", "keyword_count", "comment_count", "avg_variable_name_length", "word_count", "passing_rate", "avg_score"]
    # metrics = ["line_count", "passing_rate", "avg_score"]
    # print('problems: ', problems)
    # problems = ["2_C", "9_E", "39_E", "42_B", "53_E", "69_D", "121_C", "132_C", "193_E", "200_C"] #long
    # problems = ["2_C", "9_E", "39_E", "42_B", "53_E"]
    # problems = ["8_B", "8_E", "9_D", "14_E", "16_B", "17_A", "18_A", "27_E", "30_B", "31_E"] # medium
    # problems = ["17_A", "18_A", "27_E", "30_B", "31_E"]
    # problems = ["11_B", "20_A", "23_A", "26_A", "32_B", "32_C", "39_D", "41_C", "43_B", "55_A"]
    problems = ["11_B", "20_A", "23_A", "26_A", "32_B"]
    # problems = ["32_C", "39_D", "41_C", "43_B", "55_A"]
    metrics = ["avg_score", "passing_rate"]
    # metrics = ['line_length']
    # metrics.extend(problems)
    # print('metrics: ', metrics)
    # metrics = ["line_count"]
    # timestamp = '2025-06-19_14-18-09'
    # timestamp = '2025-06-16_14-15-27'
    # timestamp = '2025-06-19_17-37-11'


    # classifier_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_classifier_metrics.json"
    # with open(classifier_metrics_file, "r") as f:
    #     classifier_data = json.load(f)

    # decoding_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_decoder_metrics.json"
    # with open(decoding_metrics_file, "r") as f:
    #     decoding_data = json.load(f)

    #### Encoding Metrics
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
    # timestamp = '2025-08-14_15-28-06'
    problem_metrics_file = f"{ROOT_DIR}/data/{problems_dir_name}/metrics/{timestamp}_metrics.json"
    with open(problem_metrics_file, "r") as f:
        data = json.load(f)
    df_enc = pd.DataFrame(data)

    metrics = ['metric1', 'metric2', ..., 'metric12']  # Your 12 metric names

    # def create_metric_figure(metrics_subset, fig_title):
    #     """Helper function to create a figure for a subset of metrics"""
    
    # for ax, metric in zip(axes, metrics_subset):

    fig1, axes = plt.subplots(5, 1, figsize=(20, 16), sharex=True)
    axes = axes.flatten()


    for ax, problem in zip(axes, problems):
        # First, plot the BASELINE_METRIC - avg score (in all subplots)
        for i in range(len(df_enc)-1):
            color = 'gray'  # Distinct color for baseline
            alpha = 0.5  # Make it semi-transparent
            ax.plot(
                df_enc['iter'].iloc[i:i+2],
                df_enc['avg_score'].iloc[i:i+2],
                color=color,
                linestyle=':',
                alpha=alpha,
                marker='d'  # Diamond marker for baseline
            )
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
        for i in range(len(df_enc)-1):
            color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
            marker = 'o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
            
            ax.plot(
                df_enc['iter'].iloc[i:i+2],
                df_enc[problem+"_readability"].iloc[i:i+2],
                color + '-',
                marker=marker
            )
        
        ax.set_title(problem)
        ax.grid(True)

    # Add common legend
    handles = [
        plt.Line2D([], [], color='gray', linestyle=':', marker='d', label='Readability'),
        # plt.Line2D([], [], color='purple', linestyle='--', marker='x', label='Passing Rate'),
        plt.Line2D([], [], color='b', marker='o', linestyle='-', label='Encoder'),
        plt.Line2D([], [], color='r', marker='s', linestyle='-', label='Decoder')
    ]
    fig1.legend(handles=handles, loc='lower center', ncol=2)

    # Fig 2:

    fig2, axes = plt.subplots(5, 1, figsize=(20, 16), sharex=True)
    axes = axes.flatten()


    for ax, problem in zip(axes, problems):
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
        for i in range(len(df_enc)-1):
            color = 'purple'  # Distinct color for baseline
            alpha = 0.5  # Make it semi-transparent
            ax.plot(
                df_enc['iter'].iloc[i:i+2],
                df_enc['passing_rate'].iloc[i:i+2],
                color=color,
                linestyle='--',
                alpha=alpha,
                marker='x'  # Diamond marker for baseline
            )

        # Next, plot each problem metric in its own subplot
        for i in range(len(df_enc)-1):
            color = 'b' if df_enc['stage'].iloc[i] == 'encoder' else 'r'
            marker = 'o' if df_enc['stage'].iloc[i] == 'encoder' else 's'
            
            ax.plot(
                df_enc['iter'].iloc[i:i+2],
                df_enc[problem+f"_passing_rate"].iloc[i:i+2],
                color + '-',
                marker=marker
            )
        
        ax.set_title(problem)
        ax.grid(True)

    # Add common legend
    handles = [
        # plt.Line2D([], [], color='gray', linestyle=':', marker='d', label='Avg Score'),
        plt.Line2D([], [], color='purple', linestyle='--', marker='x', label='Passing Rate'),
        plt.Line2D([], [], color='b', marker='o', linestyle='-', label='Encoder'),
        plt.Line2D([], [], color='r', marker='s', linestyle='-', label='Decoder')
    ]
    fig2.legend(handles=handles, loc='lower center', ncol=2)

    fig1.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_readability.png", bbox_inches='tight', dpi=300)
    fig2.savefig(f"{ROOT_DIR}/outputs/figures/{cfg.algorithm}_{timestamp}_passing_rate.png", bbox_inches='tight', dpi=300)

    plt.tight_layout()
    plt.show()
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