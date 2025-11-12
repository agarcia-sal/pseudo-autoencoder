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
from evaluation.utils import save_metrics, save_prompt, get_pseudocode_dataset, evaluate_classifier_prompt, save_classifier_score, record_previous_best_solution, get_avg_test_case_length, get_num_difficulty, copy_difficulty_problems, get_positive_labels, write_dataset_to_file, write_error_strings_to_file, reformat_human_eval_file, get_pseudocode_dataset_test, get_pseudocode_labels, print_feedback_from_file, evaluate_classifier_prompt_test
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
        from agents.greedy_refine import GreedyRefine as ga
    elif cfg.algorithm == "direct-answer":
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

    if (evolving_encoding or evolving_decoding or evolving_cosmetic or evolving_classifier) and not load_previous: 
        setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 2) # plus 2 because of the final encoder and decoder verification at the end

    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}") # [TO DO]: decide if i still need this
    generated_prompts_path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    metrics_path = f"{ROOT_DIR}/data/{problems_dir_name}/metrics"


        # previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{iteration}", "previous_best", previous_best.json)
    # print(f"Directory '{generated_prompts_path}' created successfully")
    # print('prompt path: ', str(generated_prompts_path))

    # client = OpenAI(
    #     # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    #     api_key = os.getenv('OPENAI_API_KEY'),
    # )
   

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
        
    prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_decoder_prompt.txt")
    # profiler = cProfile.Profile()
    # profiler.enable()
    prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_decoder_prompt.txt")
    prev_encoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_encoder_prompt.txt")

    # previous_timestamp = '2025-09-18_21-00-18'
    # # previous_timestamp = '2025-09-18_04-55-13'

    # previous_timestamp = '2025-09-24_15-05-02'
    # final_iter = 34
    # prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")
    prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_decoder_prompt.txt")

    # Run for 20/64 iterations
    for it in range(starting_iteration, iterations + 1):
        # Encoding:
        if evolving_encoding:
            stage = 'encoder'
            try: # may hit an LLM rate limite
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                # for round in range(rounds):
                print('right before calling agent.step()')
                final_iter = 33
                prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_encoder.txt")
                # prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_encoder_prompt.txt")
                # prompt = encoding_agent.step()
                # print('right after calling agent.step()')
                prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_encoder_prompt.txt")

                # print('prompt from agent.step() looks like: ', prompt)
                if prompt is None:  # agent decides to terminate
                    # print('prompt is none')
                    break
                print('right before calling evaluate()')
                feedback = evaluator.evaluate(prompt, prev_decoder_prompt, stage, timestamp, it, client)  # Run evaluation
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                
                
                # UNCOMMENT BELOW:
                # encoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback
                # previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                # previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = encoding_agent.get_previous_best()
                # record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)
                
                # UNCOMMENT BELOW:
                # Get the final solution
                # if it % rounds == 0: # about to switch over to the next stage
                #     best_prompt_so_far = encoding_agent.finalize()
                #     prev_encoder_prompt = best_prompt_so_far

                # print('right after calling fnalize()')
                # if feedback.dev_score == 1.0:
                #     print('prompt: ')
                #     print(prompt)
                #     break
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                traceback.print_exc()
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
                decoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback
                # Record Previous best
                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = decoding_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)
                # Get the final solution
                # print('right before calline finalize()')
                if it % rounds == 0: # about to switch over to the next stage
                    best_prompt_so_far = decoding_agent.finalize()
                    prev_decoder_prompt = best_prompt_so_far

            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round
        if (evolving_encoding or evolving_decoding) and it % rounds == 0: # maybe start at iterations = 1 ? and put this at the bottom of the loop
            evolving_encoding = not evolving_encoding
            evolving_decoding = not evolving_decoding

    # Finalize:
    if (evolving_encoding or evolving_decoding) and iterations > 1:
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
        save_prompt(str(generated_prompts_path), prompt, iterations + 2, 'decoder')
        feedback = evaluator.evaluate(prompt, prev_encoder_prompt, 'decoder', timestamp, iterations + 2, client)
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, 'decoder', iterations + 2)


    # run final encoding and decoding prompts on the direct answer pipeline to get labels
    trivial_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_decoder_prompt.txt")
    trivial_encoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_encoder_prompt.txt")

    # run_direct_answer_pipeline(encoding_prompt, decoding_prompt, file_name)
    # print(feedback.test_feedback)  # Test set score < this is maybe where i can get the metrics [TO DO]!

    # profiler.disable()

    # Save results to file
    # stats = pstats.Stats(profiler)
    # stats.dump_stats('profile_results.prof')
    # stats.print_stats()
    # stats.sort_stats('time').print_stats(20)

    # print('best encoding prompt: ')
    # print(prev_encoder_prompt)
    # print('best decoder prompt:')
    # print(prev_decoder_prompt)

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

    store_pseudocode = False
    if store_pseudocode:
        print('in store pseudocode')
        stage = 'encoder'
        # timestamp = '2025-06-16_14-15-27'
        first_timestamp = '' # <- passing rate + natural language + conciseness
        # first_timestamp = '2025-09-18_21-00-18' # <- passing rate + natural language
        # first_timestamp = '2025-09-18_04-55-13'
        # first_timestamp = '2025-09-18_21-00-18'
        # first_timestamp = '2025-09-24_15-05-02'
        # first_timestamp = '2025-09-25_22-10-58'
        first_timestamp = '2025-09-29_10-32-52'
        first_dir_name = 'human_eval'
        # first_timestamp = '2025-09-26_19-55-20'
        # first_dir_name = 'leet_code'
        first_pipeline_json_path_name = f"{ROOT_DIR}/data/{first_dir_name}/metrics/{first_timestamp}_metrics.json"
        # second_timestamp =  '2025-09-18_21-00-18' # <- just readability: avg_word_length - avg_words_per_line
        # second_timestamp =  '2025-09-19_11-38-47'
        # second_timestamp =  '2025-09-20_00-16-56'
        # second_timestamp =  '2025-09-24_18-22-37'
        # second_timestamp =  '2025-09-24_23-50-30'
        # second_timestamp =  '2025-09-20_19-13-22'
        second_timestamp =  '2025-09-29_04-57-21'
        second_dir_name = 'cosmetic_pseudocodes'
        # second_dir_name = 'leet_code'
        second_pipeline_json_path_name = f"{ROOT_DIR}/data/{second_dir_name}/metrics/{second_timestamp}_metrics.json"
        # problems_dir_file_name = "HumanEval.jsonl"
        # problems_filename = f'LeetCodeDataset-v0.3.0tiny-train.jsonl'
        # problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        # problems_dir = f"{ROOT_DIR}/data/{first_dir_name}"
        # first_problems_filename = f'LeetCodeDataset-v0.3.0-hard-test.jsonl'
        first_problems_filename = f'HumanEval-test.jsonl'
        first_dir = f"{ROOT_DIR}/data/{first_dir_name}"
        second_dir = f"{ROOT_DIR}/data/{second_dir_name}"
        # second_problems_filename = f"positive_labels_{first_timestamp}.jsonl"
        second_problems_filename = f"pseudocode_labels_{first_timestamp}.jsonl"
        # second_problems_filename = f'LeetCodeDataset-v0.3.0-hard-train.jsonl'
        # positive_labels_path_name = os.path.join(ROOT_DIR, "outputs", "pseudocodes", f"positive_labels_{timestamp}")
        # GET POSITIVE EXAMPLES:
        # first_timestamp = '2025-09-18_21-00-18'
        # first_timestamp = '2025-09-24_15-05-02'
        
        # new_file_name = os.path.join(ROOT_DIR, "data", "cosmetic_pseudocodes", f"positive_labels_{first_timestamp}.jsonl")
        # positive_examples = get_positive_labels(first_pipeline_json_path_name, first_dir, first_problems_filename, new_file_name, first_timestamp)
        # positive_examples = get_positive_labels(first_pipeline_json_path_name, problems_dir, problems_filename, first_timestamp, iterations)

        # GET PSEUDOCODES FROM THE AUTOENCODER PIPELINE
        # first_timestamp = '2025-09-25_22-10-58'
        # first_timestamp = '2025-09-24_15-05-02'
        first_timestamp = '2025-09-29_10-32-52'
        first_timestamp = '2025-09-26_19-55-20'
        new_file_name = os.path.join(ROOT_DIR, "data", "cosmetic_pseudocodes", f"pseudocode_labels_{first_timestamp}.jsonl")
        # pseudocode_examples = get_pseudocode_labels(first_pipeline_json_path_name, first_dir, first_problems_filename, new_file_name, first_timestamp)
        
        # GET PSEUDOCODE DATASET FOR THE CLASSIFIER:
        limit = 150
        # problem_results, dev_set_results = get_pseudocode_dataset(first_pipeline_json_path_name, second_pipeline_json_path_name, first_dir, second_dir, first_problems_filename, second_problems_filename, first_timestamp, second_timestamp, iterations, limit)

        # GET PSEUDOCODE TEST DATASET FOR THE CLASSIFIER
        # first_timestamp = '2025-09-25_22-10-58'
        first_timestamp = '2025-09-24_15-05-02'
        # first_timestamp = '2025-09-29_10-32-52'
        first_dir_name = 'cosmetic_pseudocodes'
        first_dir = f"{ROOT_DIR}/data/{first_dir_name}"
        # second_timestamp = '2025-09-26_02-36-01'
        # second_timestamp = '2025-09-29_10-50-33'
        second_timestamp = '2025-09-29_13-46-17'
        second_pipeline_json_path_name = f"{ROOT_DIR}/data/{first_dir_name}/metrics/{second_timestamp}_metrics.json"
        first_problems_filename = os.path.join(ROOT_DIR, "data", "cosmetic_pseudocodes", f"pseudocode_labels_{first_timestamp}.jsonl")
        limit = 150
        problem_results = get_pseudocode_dataset_test(second_pipeline_json_path_name, first_dir, first_problems_filename, second_timestamp, limit)
        version = 2
        # test_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-test.jsonl" )
        test_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-train.jsonl" )
        write_dataset_to_file(problem_results, test_set_filename)
        # print('problem_results: ')
        # print(problem_results)
        # print('dev_set_results:')
        # print(dev_set_results)
        # true_positive_examples, true_negative_examples, near_miss_examples, near_pass_examples = results
        version = 1
        # train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-train.jsonl" )
        # dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-dev.jsonl")
        # write_dataset_to_file(problem_results, train_set_filename)
        # write_dataset_to_file(dev_set_results, dev_set_filename)
        # write_dataset_to_file(positive_examples, positive_examples_file_name)
        # [TO DO]: add near-misses, and near-passes as something i get from the pseudocode dataset
        # For train:
        previous_timestamp = '2025-09-18_04-55-13'
        final_iter = 34
        decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")
        version = 2
        file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        # file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        version = 3
        new_file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl")
        # new_file_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-train.jsonl" )
        # write_error_strings_to_file(file_name, new_file_name, decoder_prompt, client)
        # split = "test"
        # problems_filename = f'HumanEval-{split}.jsonl'
        # file_name = os.path.join(ROOT_DIR, "data", "human_eval", problems_filename)
        # reformat_human_eval_file(file_name)
        # previous_best_timestamp = '2025-09-25_15-00-26'
        # current_iter = 16
        # previous_best_file_path = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", "outputs", previous_best_timestamp, f"iter_{current_iter}", "previous_best", "previous_best.json")
        # print_feedback_from_file(previous_best_file_path)


    ######################## Create cosmetic changes for the positive labels: ################################

    cosmetic_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='cosmetic'
    )
    # evolving_cosmetic = True
    cosmetic_iterations = 16

    if load_previous and evolving_cosmetic:
        prev_iter = 0
        cosmetic_previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{prev_iter}", "previous_best", "previous_best.json")
        cosmetic_agent.load_previous(cosmetic_previous_best_path)

    evaluator_cosmetic = Evaluator(data, timeout=5) # [TO DO]: change timeout
    # positive_examples_file_name = os.path.join(ROOT_DIR, "outputs", "pseudocodes", f"positive_labels_{timestamp}.jsonl")
    
    # previous_timestamp = '2025-09-18_21-00-18'
    # previous_timestamp = '2025-09-18_04-55-13'
    # previous_timestamp = '2025-09-24_15-05-02'
    # previous_timestamp = '2025-09-25_22-10-58'
    previous_timestamp = '2025-09-26_19-55-20'
    # positive_examples_file_name = f"positive_labels_{previous_timestamp}.jsonl"

    final_iter = 34
    previous_timestamp = '2025-09-18_21-00-18'

    decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_decoder_prompt.txt")

    # decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")

    #[TO DO]: set up dataset and metrics path and everything else.

    for it in range(1, cosmetic_iterations+1):
        # Encoding:
        if evolving_cosmetic:
            stage = 'cosmetic'
            try: # may hit an LLM rate limite
                
                # print('right before calling agent.step()')
                prompt = cosmetic_agent.step()
                # print('step:', 0)
                # print('right after calling agent.step()')
                # print('prompt from agent.step() looks like: ', prompt)
                if prompt is None:  # agent decides to terminate
                    print('prompt is none')
                    break
                print('right before calling evaluate() within the round')
                feedback = evaluator_cosmetic.evaluate_cosmetic(prompt, decoder_prompt, stage, timestamp, it, client)
                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                
                # [TO DO]: add a try except or catch error when there is not an encoder prompt returned
                cosmetic_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback
                # Record Previous best:
                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = cosmetic_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)

                #######################################################################
              
            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round

    ######################## Run the classifier: ####################################################
    generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}")
    generated_prompts_path.mkdir(parents=True, exist_ok=True)

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
    # evolving_classifier = False
    classifier_iterations = 32
    # rounds = 1
    # UNCOMMENT:

    # previous_timestamp = '2025-09-18_21-00-18'
    # final_iter = 34
    # decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")
    # decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_decoder_prompt.txt")
    # previous_timestamp = '2025-09-18_21-00-18'
    previous_timestamp = '2025-09-24_15-05-02'
    final_iter = 34
    decoder_prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")

    evaluator_classifier = Evaluator(data, timeout=5)

    for it in range(1, classifier_iterations + 1):
        # Encoding:
        if evolving_classifier and False:
            stage = 'classifier'
            try: # may hit an LLM rate limite
                # reevo = ga(cfg, ROOT_DIR, stage, round, timestamp, client) # maybe i should have different clients for generating and for reflecting
                # best_prompt_overall, best_prompt_path_overall = reevo.evolve()
                # run_results(best_prompt_overall, best_prompt_path_overall, stage, problems_dir_name, timestamp, round)
                
                # UNCOMMENT:
                # prompt = classifier_agent.step_direct_answer()
                prompt = classifier_agent.step()

                # prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_classifier.txt")
                
                if prompt is None:  # agent decides to terminate
                    # print('prompt is none')
                    break
                save_prompt(str(generated_prompts_path), prompt, it, stage)
                # print('right before calling evaluate() within the round')
                # feedback = evaluator_classifier.evaluate_classifier(prompt, decoder_prompt, stage, timestamp, it, client)
                mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client)
                # mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client, decoder_prompt, classifier_dataset_name, timestamp, it)
                # print('step:', 1)
                feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
                # feedback = evaluator_classifier.get_feedback_classifier(mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
                # print('step:', 2)
                score = feedback.dev_score
                # save_classifier_score(score, metrics_path, timestamp, stage, it)
         
                # UNCOMMENT:
                classifier_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback

                avg_metrics = feedback.avg_metrics
                save_metrics(avg_metrics, metrics_path, timestamp, stage, it)

                # UNCOMMENT:
                previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
                previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = classifier_agent.get_previous_best()
                record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)

            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                continue  # Skip to the next round

    # [TO DO]: do a final accuracy check on the final prompt. oh but isnt that evaluate_classifier_prompt() should do above?
    # test the final prompt with the TEST dataset
    
    if evolving_classifier:
        # test final classifier prompt with dev_set and test_set
        # UNCOMMENT PROMPT BELOW:
        prompt = classifier_agent.finalize()

        # previous_timestamp = '2025-09-25_14-14-02'
        # timestamp = '2025-09-25_13-37-25'
        # timestamp = '2025-09-25_15-00-26'
        # timestamp = '2025-09-25_15-41-49'
        # timestamp = '2025-09-25_17-46-20'
        # timestamp = '2025-09-25_18-36-13'
        # final_iter = 34
        # prompt = file_to_string(f"{ROOT_DIR}/outputs/prompts/{previous_timestamp}/prompt_iter_{final_iter}_decoder.txt")
        # prompt = "Given any input pseudocode which may include classes, functions, variables, control flow constructs (loops, conditionals, recursion), and data manipulation steps, determine **with complete and unequivocal certainty** whether the pseudocode is **fully reproducible**. Here, *fully reproducible* means that the pseudocode can be directly converted into a working implementation that passes **all unit tests without any modification, supplementation, or correction**.\n\n---\n\n### Instructions for Evaluation:\n\nYou must output exactly one digit per input pseudocode:\n- Output `1` if and only if the pseudocode satisfies **all** criteria below and can be guaranteed to pass **every** unit test exactly as given.\n- Output `0` if any criterion is not met, or if there remains **any reasonable doubt** about reproducibility or correctness.\n\nNo explanations, no whitespace, no extra characters\u2014only a single digit `1` or `0` per input pseudocode, in exact input order.\n\n---\n\n### Comprehensive Criteria for Full Reproducibility:\n\n1. **Complete, Explicit, and Self-Contained Definitions:**\n   - All functions, methods, classes, and procedures used anywhere are fully and explicitly defined in the pseudocode.\n   - No references to undefined functions, libraries, or external modules beyond common, well-known primitives explicitly permitted.\n   - Function/method signatures must state all parameters (with types or clearly defined roles) _and_ return types if applicable.\n   - All nested functions or helpers must be defined within accessible scope.\n\n2. **Syntactic and Semantic Clarity and Precision:**\n   - The pseudocode syntax is sufficiently explicit and precise to be mechanically translated into executable code without ambiguity.\n   - Loops and conditionals clearly indicate exact iteration bounds, termination conditions, and case coverage.\n   - Recursive functions explicitly include clearly defined and reachable base cases ensuring termination.\n   - All control flows (including breaks, continues, exceptions if any) are fully spelled out without ambiguity or multiple possible interpretations.\n\n3. **Consistent and Unambiguous Naming and Scope Resolution:**\n   - Every variable, function, class, or object is declared before use.\n   - Names are consistent and not ambiguous or conflicting.\n   - Variable scopes (global, local, closures) are directly inferable from the pseudocode without assumptions.\n   - No identifiers are introduced implicitly or without definitions.\n\n4. **Explicit Initialization and Type Clarity:**\n   - Every variable is initialized or assigned a valid value before any usage.\n   - Data types or roles of variables, function arguments, arrays, and data structures are explicitly stated or can be unambiguously deduced.\n   - Data structures specify their type, dimensions, content if initialized, and all modifications clearly.\n\n5. **Complete and Explicit Edge Case and Exception Handling:**\n   - The pseudocode explicitly accounts for all typical and edge input cases known to be covered by unit tests (including empty inputs, maximal/minimal values, unusual values, boundary conditions).\n   - No branches, cases, or inputs are omitted or left implicit.\n   - Fail-safe guards against invalid accesses, divisions by zero, null dereferences, or other runtime errors are present where required.\n\n6. **Logical Consistency and Exhaustiveness:**\n   - The pseudocode is free from contradictions, logical gaps, or unintentionally missing steps.\n   - Intermediate computational steps are fully specified when essential for correctness.\n   - No shortcuts, partial implementations, or reliance on external explanations.\n\n7. **Robustness Against Runtime Errors and Structural Faults:**\n   - No usage of undefined or uninitialized variables, functions, or data structures.\n   - Return statements correctly appear in all function exit paths where a return is expected.\n   - No illegal operations such as out-of-bound indexing without conditional protection.\n   - All loop constructs and conditional branches are properly opened and closed, with no malformed flows.\n   - All function and method calls match their declared signatures consistently.\n\n8. **Guaranteed Passing of 100% Unit Tests:**\n   - The pseudocode represents a fully correct algorithm according to the problem\u2019s specification.\n   - It must be robust against all inputs and edge cases that typical unit tests would exercise.\n   - Partial or near misses (e.g. passing 80% or 99%) are not sufficient \u2014 all tests must pass.\n\n9. **Self-Contained Implementation Without External Dependency:**\n   - No required logic, data, or calls missing from the pseudocode that would need to be \"filled in\" externally.\n   - Only well-known, standard language primitives and constructs are allowed as implicit assumptions.\n   - No calls to non-standard or unspecified external systems, libraries, or environment-specific features.\n\n10. **Permissible Variations:**\n    - Formatting style, indentation, variable naming conventions, and minor syntactic differences are acceptable as long as they do not introduce ambiguity or incompleteness.\n    - Logical equivalence overrides superficial differences.\n\n---\n\n### Stepwise Evaluation Procedure:\n\n- Parse the entire pseudocode accurately, including all nested scopes.\n- Confirm presence and precise definitions of all required components.\n- Verify that all used variables, functions, and classes are declared, initialized, and consistent.\n- Validate all control structures are fully specified with clear boundaries and termination.\n- Confirm explicit coverage of expected edge cases and error guards.\n- Detect any contradictions, missing logic, or implicit assumptions that would preclude successful execution.\n- Assume no unknown implicit behaviors; any unavoidable doubt leads to a `0`.\n- Accept stylistic freedoms that do not obscure or omit required logic.\n- Remember: perfect reproducibility is mandatory for a `1`.\n\n---\n\n### Output Format:\n\nFor each pseudocode input processed, output a single digit, either:\n\n- `1` (fully reproducible and guaranteed to pass all unit tests as-is), or\n- `0` (otherwise, including any ambiguity or partial correctness).\n\nNo additional text, no line breaks, no commentary\u2014only the digit per input, in order.\n\n---\n\n**Example:**\n\nInput pseudocode:  \n```\nCLASS Solution  \n    FUNCTION sumToN(n) RETURNS integer  \n        SET total TO 0  \n        FOR i FROM 1 TO n  \n            INCREMENT total BY i  \n        END FOR  \n        RETURN total  \n    END FUNCTION  \nEND CLASS\n```\n\nOutput:  \n`1`\n\n---\n\n**Strictness reminder:**  \nIf any missing component, ambiguous part, potential runtime error, or partial correctness is found, output `0`. Only flawless, fully explicit, and logically sound pseudocode compliant with all above criteria merits `1`.\n\n---\n\n**Your task:** Using these instructions and criteria, determine reproducibility of each provided pseudocode input **with maximal precision**.\n\n---\n\n**End of prompt.**"
        # prompt = "Given a pseudocode description of a complete function or class method intended to solve a well-defined programming problem, your task is to determine with absolute certainty whether this pseudocode is fully reproducible\u2014meaning that *any* direct, faithful implementation derived solely and unambiguously from it will pass **all** valid unit tests relevant to the problem, without fail.\n\nYou must respond strictly with a single digit \u2014 **1** if and only if the pseudocode meets **all** of the criteria below, or **0** otherwise. Provide no explanations, comments, or additional text. The outputs must be in the same order as the pseudocodes are given.\n\nTo confidently decide, verify all of the following conditions rigorously:\n\n1. **Complete and Explicit Problem Definition:**  \n   The pseudocode clearly specifies or unambiguously implies the problem\u2019s input domain(s), output expectations (type and format), and all required invariants or constraints without relying on external context or assumptions.\n\n2. **Fully Specified Interface and Signature:**  \n   The function or method signature is explicit and self-contained, fully stating input parameter names and types, return type, and encapsulation context (class or module scope). The interface matches the problem requirements exactly.\n\n3. **Deterministic and Exhaustive Logic Specification:**  \n   All algorithmic steps, including control flow constructs (loops, recursion, conditionals), data initializations, updates, and termination conditions, are described completely and unambiguously. Boundary conditions, loop invariants, and recursive base/inductive cases are explicitly handled without gaps.\n\n4. **Explicit Edge Case and Exceptional Handling:**  \n   All relevant edge cases, special input scenarios, and error conditions are addressed explicitly or logically guaranteed by the described algorithm. No inputs can cause undefined, partial, or ambiguous behavior.\n\n5. **Unambiguous Instructions and Operations:**  \n   Each operation (arithmetic, indexing, string manipulation, data structure modification) is specified with precise semantics. Avoid shorthand notations, ambiguous variable references, or symbolic shorthand that require interpretation beyond plain reading.\n\n6. **Logical Coherence and Internal Consistency:**  \n   There are no conflicting statements, missing steps, or logical omissions. The flow of data and control must be consistent and sequentially coherent; necessary intermediate computations or data structure states must be accounted for.\n\n7. **Structural Completeness and Implementability:**  \n   The pseudocode is sufficiently structured and complete so that it can be translated directly into syntactically correct, executable source code in a conventional programming language without any guessing, assumptions, or added scaffolding.\n\n8. **Explicit Enforcement of Constraints and Domain Rules:**  \n   Any problem-specific rules, limitations, or invariants critical for correctness (e.g., input bounds, resource limits, ordering constraints) are expressly enforced or guaranteed by the logic.\n\n9. **Self-Containment \u2014 No External Dependencies:**  \n   The pseudocode must be a self-sufficient specification: it cannot depend on unstated helper routines, unavailable libraries, external resources, or omitted steps. Every part crucial to correctness must be included or fully described.\n\n10. **Tolerance to Notational and Stylistic Variations:**  \n    Variations in variable/function naming, formatting, or permissible language-agnostic style differences that do *not* affect logical completeness or correctness are acceptable and must not cause rejection.\n\n11. **Presence and Correct Use of Function or Class Context:**  \n    The pseudocode includes all necessary declarations to ensure correct binding, accessibility, and namespace resolution (e.g., class definitions, method visibility) so the code can be instantiated and invoked as intended by automated tests.\n\n12. **No Ambiguity Regarding Mutability and Side Effects:**  \n    Any modification of input data structures or use of mutable state must be clearly defined and consistent with problem specifications; side effects must be well-detailed to guarantee faithful reproduction in real code.\n\n**Critical:** If you identify *any* uncertainty, incompleteness, ambiguity, logical gap, missing interface detail, or partial coverage that could lead to some faithful implementations derived from the pseudocode failing one or more unit tests, output **0**. Do *not* guess or assume missing information. The default conservative answer is zero unless fully confident.\n\n---\n\nOutput exactly one digit (1 or 0) for each pseudocode input, in the order provided, and nothing else."
        # prompt = "```\nTask:  \nYou will receive one or more pseudocode snippets, each describing the full logic of a solution to an unspecified computational problem. For each snippet, output exactly one digit:  \n- `1` if the pseudocode is *fully reproducible*, meaning that **any faithful implementation directly and strictly following this pseudocode (without adding, omitting, or guessing any detail) will pass every possible unit test verifying full correctness**, including normal, edge, boundary, error, invalid, and corner cases within the problem scope.  \n- `0` otherwise.  \n\nOutput:  \n- Concatenate all output digits in the input snippet order, with no spaces, newlines, or any other characters.  \n- Output nothing else (no explanations or formatting).  \n\nDefinition of *fully reproducible*:  \nA pseudocode snippet is *fully reproducible* if it unambiguously and exhaustively specifies an algorithm guaranteed to:  \n\n1. **Handle all valid and relevant invalid inputs explicitly or logically**  \n   - Define input domain, types, and constraints without unstated assumptions.  \n   - Address or safely tolerate empty inputs, zero-length structures, null-equivalents, boundary values, malformed or out-of-spec inputs within problem scope.  \n   - Reject or handle invalid inputs if expected by the problem; otherwise, explicitly exclude them.  \n   - Do *not* rely on external input validation or assumptions beyond the pseudocode.  \n\n2. **Define all variables, data structures, and state fully and clearly**  \n   - Declare and initialize every variable before use, including indices, counters, accumulators, flags, temporary values, and complex structures.  \n   - No use of undefined variables, implicit defaults, or externally defined symbols or types.  \n   - Explicitly specify data structures\u2019 sizes, initial values, and contents where relevant.\n\n3. **Specify deterministic, complete, and sound control flow and logic**  \n   - All loops and recursion have well-defined entry, progress, and termination conditions ensuring no infinite loops or premature exits that violate correctness.  \n   - Conditionals and switch statements collectively cover all relevant input and intermediate states with no ambiguous or omitted branches.  \n   - No logically contradictory, conflicting, or unreachable code affecting outcome correctness.  \n   - Every control path is well explained and fully covered.\n\n4. **Provide detailed, unambiguous, and correct algorithmic steps**  \n   - Every computational step, update, mutation, comparison, and operation is explicit, logically consistent, and accurately captures the intended algorithm.  \n   - No gaps, vague descriptions, or missing essential operations.  \n   - Arithmetic or indexing operations are clearly defined and respect data boundaries.\n\n5. **Explicitly handle all boundaries, edge cases, and exceptional or failure conditions**  \n   - Boundary values (e.g., minimal and maximal inputs, empty data, zero divisors, possible overflow/underflow cases) are checked and correctly handled.  \n   - Contains safeguards or checks avoiding undefined or erroneous states (e.g., out-of-range accesses, invalid memory/state).  \n   - Error handling or alternative flows for invalid or exceptional inputs are specified if the problem domain requires them.\n\n6. **Define outputs precisely and deterministically**  \n   - Output values, formats, and types are explicitly given and unmistakably derived from prior computation steps.  \n   - Intermediate and final outputs have no ambiguity about their construction or meaning.  \n   - Output format complies fully with expected problem output conventions.\n\n7. **Require no external context, unstated assumptions, or hidden dependencies**  \n   - The snippet is fully self-contained and implementable as-is, relying only on primitives explicitly defined within or universally understood in pseudocode context.  \n   - Does *not* depend on external libraries, environment, data, language features, or implicit behaviors.  \n   - No need for reader or implementer to infer or fill any missing detail.\n\n8. **Maintain clarity, consistency, and precision in style and notation**  \n   - Pseudocode syntax and idioms must be clear; style variations are allowed only if they maintain unambiguous semantics and full logical completeness.  \n   - Avoid overly terse, ambiguous, or inconsistent expressions that lead to conflicting interpretations.  \n   - Ambiguity in control flow, state changes, or output caused by style issues invalidates reproducibility.\n\n**Evaluation instructions:**  \n- Carefully and conservatively analyze each snippet according to all 8 criteria.  \n- If *any* uncertainty, missing detail, ambiguity, incompleteness, or logical gap exists that could cause any conceivable failing unit test, return `0`.  \n- Output `1` *only if* the snippet meets *all* criteria rigorously and completely.  \n- This includes full functional correctness across the entire expected input/output domain, not just typical or common cases.  \n\n**Additional strict notes:**  \n- Do *not* guess or supply any missing details or constraints, even if intuitively obvious.  \n- Do *not* tolerate implicit assumptions about input validity, environment or language behavior, or implementation details.  \n- Thoroughly consider the snippet\u2019s behavior on edge cases, invalid cases (if applicable), corner cases, and complex logical scenarios.  \n- Guard against subtle reproducibility pitfalls: uninitialized states, implicit default values, overlooked boundary conditions, ambiguous returns, infinite loops or recursion, and partial or incomplete logic coverage.  \n\n---\n\nPseudocode:  \n```<INSERT_PSEUDOCODE_HERE>```\n```"
        # prompt = "```\nYou will be provided one or more pseudocode snippets, each claiming to fully describe a complete solution to some computational problem.\n\nYour task: For each snippet, independently determine whether it is **REPRODUCIBLE** \u2014 that is, if implemented exactly as given, without any external information, guesses, or assumptions, it will pass **all** relevant unit tests without fail.\n\nOutput a single digit for each snippet in the input order:  \n- `1` if it meets **all** criteria of reproducibility  \n- `0` otherwise  \n\nOutput only these digits, one per line, with no extra text or formatting.\n\n---\n\nTo rigorously assess **REPRODUCIBILITY**, apply the following detailed criteria:\n\n1. **Complete and Explicit Specification**  \n   - All variables, data structures, inputs, and outputs are fully declared or unambiguously implied.  \n   - Every step needed to implement the solution is clearly and explicitly described (including initializations, iterations, conditionals, and returns).  \n   - Edge cases and special conditions are explicitly handled.  \n   - No aspect of the logic or control flow may be left incomplete, vague, or ambiguous.  \n   - Do NOT fill in or infer unstated details beyond what is presented.\n\n2. **Soundness and Correctness of Logic**  \n   - The algorithmic reasoning correctly handles *every* valid input case, including edge cases.  \n   - There are no logical errors, contradictions, infinite loops, or unreachable code segments.  \n   - Mentally simulate the pseudocode with typical and boundary inputs to check correctness.\n\n3. **Unambiguous Interpretability**  \n   - Every operation and instruction is stated with clarity such that only one precise implementation is possible.  \n   - Ambiguous terms, unclear variable scopes, or unspecified behaviors invalidate reproducibility.\n\n4. **Self-Containment and Independence**  \n   - The snippet must be fully self-sufficient, requiring no additional code snippets, helper functions, libraries, or external context.  \n   - If any auxiliary procedures or standard functions are referenced, their definitions or clear invocation context must be included.\n\n5. **Structural and Semantic Integrity**  \n   - Control structures (loops, recursion, conditionals) and data manipulations must be syntactically consistent and semantically coherent within the pseudocode\u2019s style.  \n   - Variables and data must be properly defined before use, and the flow must guarantee proper termination and result delivery.\n\n6. **Deterministic and Complete Output Definition**  \n   - The final output(s) are clearly specified, including data type and format.  \n   - Return or output statements must be unambiguous.  \n   - No partial or conditional returns that might cause uncertainty regarding final results.\n\n---\n\n**Important:**  \n- If any doubt, ambiguity, missing element, or structural flaw exists, output `0`.  \n- Only output `1` when every item above is *unquestionably* fulfilled.\n\nProceed immediately and produce only the requested output digits for the given pseudocode snippets.\n```"
        # prompt = "Given the pseudocode below, your task is to determine, **without executing or simulating**, whether the pseudocode is fully and unambiguously specified such that **any correct translation of it according to its specification will pass all unit tests exactly**.\n\nOutput **1** if and only if the pseudocode guarantees perfect reproducibility\u2014that is, a faithful implementation passing every unit test without exception\u2014and **0** otherwise.\n\nTo decide, rigorously verify that **all** of the following conditions hold strictly and completely:\n\n---\n\n### 1. **Complete Structural and Interface Definition**  \n- All functions, procedures, methods, or classes are explicitly and uniquely named.  \n- Every declared function\u2019s input parameters (names, types, counts) and return values (types, meanings) are fully specified, precise, and match exactly the expected testing framework interface. No implicit assumptions on parameter naming, ordering, optionality, default values, or return semantics allowed.  \n- All variables, constants, and data structures are explicitly declared or introduced with clear initialization or guaranteed valid initial states before use. Uninitialized or vaguely initialized entities cause failure.  \n- The pseudocode\u2019s overall structure (e.g., classes, function signatures, entry points) aligns perfectly with what the testing environment requires, including expected parameter names and data types.\n\n### 2. **Algorithmic Determinism and Exhaustiveness**  \n- Every control flow construct (loops, recursions, conditionals) is detailed with **explicit and unambiguous conditions**, exact loop bounds, and guaranteed termination proofs or provided exit conditions **covering all valid inputs**. No possibility of infinite loops or undefined iteration scenarios.  \n- Each step in the computational process is fully described: operations, state transitions, side effects, and intermediate variables\u2014all specified without dependence on external or unstated mechanics, language-specific quirks, or hidden state.  \n- The algorithm completely addresses the problem scope it implies or states, with **no implicit gaps, missing steps, or undefined behaviors** anywhere.  \n- All critical assumptions, invariants, preconditions, and postconditions affecting correctness must be **explicitly stated or unambiguously derivable** strictly from pseudocode content; nothing may be inferred beyond what is explicitly written.  \n- If any instruction or condition admits multiple plausible interpretations or allows ambiguity, the reproducibility cannot be guaranteed and you must output `0`.\n\n### 3. **Comprehensive Edge Case and Boundary Coverage**  \n- The pseudocode must explicitly handle all problem-relevant edge cases (e.g., empty inputs, zero values, minimal/maximal sizes, invalid or special inputs), or clearly and unambiguously imply their correct handling without contradiction or omission.  \n- Accesses to elements by index or position must have exact bounds and offsets defined, preventing any out-of-bound possibility or undefined memory/data access.  \n- Exceptional and corner cases must be either explicitly addressed or explicitly stated as omitted with due rationale; silent or implicit handling that risks inconsistent or undefined behavior mandates output `0`.\n\n### 4. **Implementation Independence and Full Determinism**  \n- The pseudocode is fully self-contained, with no reliance on external/global variables, hidden state, or environment beyond the declared inputs and explicit outputs.  \n- No use of randomness, non-deterministic operations, platform-dependent functionality, or unspecified ordering of operations is permitted.  \n- The output for any fixed valid input is uniquely defined and reproducible strictly from the pseudocode steps given.\n\n### 5. **Direct Implementability and Consistency with Test Harness**  \n- The pseudocode is immediately translatable into a fully functional, standalone implementation without requiring any external scaffolding, undeclared helper functions, or supplemental libraries.  \n- The interface format (function/class signatures, parameter names/types, and returns) maps exactly onto the standardized test harness expectations without adding or omitting any element.  \n- The pseudocode does not omit any critical implementation detail that would force guesswork or require environment-specific fixes.\n\n---\n\n### Additional Evaluation Details & Decision Rules  \n- Any **uncertainty** about variable initialization, function interface correctness, loop termination, or edge case handling requires output `0`.  \n- Do *not* perform guessing or \"common sense\" in filling unspecified details. Judge strictly by explicit specifications only.  \n- Contradictions, inconsistent logic, or ambiguous statements anywhere force output `0`.  \n- If structural interface details contradict expected test interfaces (e.g., different parameter names or missing return values), output `0`.  \n- Recursive or iterative flows without exact, provable termination conditions mandate output `0`.  \n- Confirm all variables, operations, and data transformations are fully traceable and precise, including intermediate or auxiliary data.\n\n---\n\n**Output instructions:**  \n- For each pseudocode input, output exactly one digit (`1` or `0`) on a separate line, in the order the pseudocodes are provided, **with no extra text, formatting, or explanation**.  \n- `1` means completely reproducible, guarantees passing all unit tests.  \n- `0` means not reproducible due to any ambiguity, incompleteness, inconsistency, or unspecified behavior.\n\n---\n\nThis prompt enforces a strict, all-encompassing reproducibility checklist emphasizing **explicitness, completeness, deterministic correctness, and exact interface alignment**\u2014maximizing accuracy in distinguishing pseudocode that truly guarantees passing unit tests from those that do not."
        # prompt = "Given one or more pseudocode snippets, each purporting to fully solve a problem, your sole task is to output a single digit (`1` or `0`) per snippet, concatenated into a single string reflecting the input order, with no spaces, punctuation, or any other characters.\n\n**Output a `1` if and only if the snippet is strictly reproducible \u2014 meaning it will deterministically pass _all possible valid unit tests_ for the stated problem, with no exceptions, failures, or undefined behavior under _any_ valid input scenario. Otherwise, output `0`.**\n\n---\n\n### Core evaluation principles (apply independently to each snippet):\n\n#### A. **Complete, Terminating, and Exhaustive Logic**  \n- The snippet fully specifies behavior covering all inputs, including edge and corner cases (empty, minimal, maximal, boundary).  \n- All control flows (loops, recursion, conditionals) conclusively terminate or produce defined results without infinite loops, deadlocks, or partial evaluations.  \n- No input branch or case is left unspecified, ambiguous, or partially handled.\n\n#### B. **Unambiguous, Self-contained Semantics**  \n- All variables, data structures, and operations used are explicitly declared, initialized, and updated within the snippet\u2014there are no hidden external dependencies, implicit states, or assumptions about a runtime environment.  \n- Data transformations and outputs are deterministic and consistent on identical inputs \u2014 no randomness, concurrency issues, or nondeterminism.  \n- No vagueness or underspecification in how computations proceed.\n\n#### C. **Algorithmic Correctness and Completeness**  \n- The snippet fully embodies a valid end-to-end algorithm that logically aligns with the problem requirements or can be soundly inferred as correct for the intended task.  \n- Partial outlines, incomplete heuristics, or mere sketches that omit critical steps or helper procedures cause failure.  \n- All auxiliary functions and procedures invoked are fully defined in the snippet or validly included in-context.  \n- Recognizable standard algorithms must be logically and structurally correct in core details (correct initialization, updates, and state transitions).\n\n#### D. **Robustness and Fault Handling**  \n- The snippet explicitly accounts for invalid inputs, exceptional/fault conditions, boundary values, numeric overflows/underflows, empty structures, and other corner cases.  \n- It either handles or explicitly excludes error conditions to avoid runtime failures, crashes, or undefined results.\n\n#### E. **Consistent Control Flow and Data Integrity**  \n- State changes occur in a logically consistent manner; there are no contradictory updates, unreachable code segments, or silent logical errors.  \n- Data dependencies and side effects are accounted for clearly within the snippet.\n\n---\n\n### Strict rules for assessment:\n\n- **Limit your analysis purely to the snippet itself, ignoring comments, formatting, variable naming, or any external context not explicitly given.**  \n- **Do not assess style, syntax variants, or superficial issues.**  \n- **If any single principle is violated, output `0` for that snippet.**  \n- **Only output `1` if the snippet meets _all_ the criteria beyond reasonable doubt.**\n\n---\n\n### Output format reminder:\n\n- Output exactly one `1` or `0` digit per snippet in input order, no spaces, no newlines, no extra text.\n\n---\n\n### Performance considerations:\n\n- Your judgment must be logically sound yet efficient enough to complete within 5 seconds per all snippets combined.  \n- Prioritize decisive, semantically precise evaluation over guesswork or partial heuristics.\n\n---\n\n**Summary**: Your role is a meticulous semantic verifier of reproducibility\u2014that is, if given these pseudocode snippets, can they be confidently regarded as fully correct, self-contained, terminating, error-free solutions guaranteed to pass _every_ valid unit test. Your output string encodes thus, per snippet, `1` for reproducible, `0` for otherwise, no more, no less."
        # prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_classifier.txt")

        generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}")
        generated_prompts_path.mkdir(parents=True, exist_ok=True)
        save_prompt(str(generated_prompts_path), prompt, classifier_iterations+1, 'classifier')
        save_prompt(str(generated_prompts_path), prompt, classifier_iterations+2, 'classifier')
        # train score:
        mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client)
        feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+1)
        # dev score:
        # dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl" )
        # mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(dev_set_filename, prompt, client, decoder_prompt, classifier_dataset_name, timestamp, classifier_iterations+2)
        # dev_feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
        # avg_metrics = dev_feedback.avg_metrics
        # save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+2)
        # test score:
        # test_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-test.jsonl" )
        version = 2
        test_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-test.jsonl" )
        avg_metrics = evaluate_classifier_prompt_test(test_set_filename, prompt, client)
        # dev_feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
        # avg_metrics = dev_feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+2)

        # DirectAnswer score:

        # test_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-test.jsonl" )
        # test_score = evaluate_classifier_prompt(test_set_filename, prompt, client)
        # test_feedback = evaluator.get_feedback_classifier(test_score)
        # avg_metrics = feedback.avg_metrics
        # save_metrics(avg_metrics, metrics_path, timestamp, stage, it)
        #[TO DO]: add adding metrics to evaluator.get_feedback
        #[TO DO]: check on save_classifier_score
        #[TO DO]: check that finalize has all the correct things, it has dev_score but should also have validation score
    
        # print('avg_metrics: ', avg_metrics)
        # save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+1)
        # save_classifier_score(dev_score, metrics_path, timestamp, "classifier", classifier_iterations+1)
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
    problems = ["HumanEval/0", "HumanEval/1", "HumanEval/2", "HumanEval/3", "HumanEval/4"]
    problems = ["two-sum", "add-two-numbers", "longest-substring-without-repeating-characters", "median-of-two-sorted-arrays", "zigzag-conversion"]
    # problems = ["32_C", "39_D", "41_C", "43_B", "55_A"]
    metrics = ["avg_score", "passing_rate"]
    # "line_count": 0.27,
    # "keyword_count": 0.02,
    # "comment_count": 0.015,
    # "avg_variable_name_length": 0.40127751466887673,
    # "word_count": 0.3313068181818181,
    # "line_length": 0.33531474263316857,
    # "avg_word_length": 0.42462834503699964,
    # "avg_syllables_per_word": 0.3109315957055333,
    # "syllable_count": 0.2621553610503282,
    # "readability": 0.5997804954915572,
    # "avg_words_per_line": 0.3634069042347718,
    # "passing_rate": 0.9461029692132255,
    # "avg_score": 2.644616349361224,
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