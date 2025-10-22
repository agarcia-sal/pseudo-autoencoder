# Pseudo-Autoencoder: Large Language Models for Examining Pseudocode Validity

# CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization


![example](https://github.com/user-attachments/assets/faf29c44-4904-4d74-9a15-37a038b14e77)

**Paper:** [CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization](https://arxiv.org/abs/2504.04310)

**Data:** [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset) and [HumanEval](https://github.com/openai/human-eval)

# Download Data
Download the raw data from [HumanEval](https://github.com/openai/human-eval) to the local directory `data/human_eval` and LeetCodeDataset-v0.3.0-train.jsonl and LeetCodeDataset-v0.3.0-test.jsonl from [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset)

# Agent Implementations

Agents are implemented in the `agents` module. Currently supported agents include: `GreedyRefine`, `DirectAnswer`

Each agent implements the following functions:
- `step()`: Returns the next candidate prompt for evaluation.
- `feedback()`: Accepts evaluation results of previous candidate prompt and returns feedback for LLM prompt.
- `finalize()`: Returns the final prompt.
- `get_previous_best()`: Returns previous best Solution so far to store at each iteration of a pipeline
- `load_previous()`: If a pipeline stops running prematurely, will return previous best solution up to that point so that the pipeline can continue running

# Pipeline selection

There are 3 pipelines available to run: Autoencoder, Cosmetic, and Classifier

Set the `evolving_encoding`, `evolving_decoding`, `evolving_cosmetic`, `evolving_classifier` flag to True depending on which pipeline you want to run. For the autoencoder pipeline, set the `evolving_encoding` to True and `evolving_decoding` flag to False to start off with. The flags will toggle as the autoencoder switches between these two stages.

Depending on which pipeline you are running, set the correct `problems_dir_name` under which you will be operating. For the autoencoder, choose either `problems_dir_name = leet_code` or `problems_dir_name = human_eval`

Set the number of iterations you want to run. Default is 32
Set number of rounds, which is the number of iterations run before switching from encoder to decoder and vice versa. Default is 2

# Results

Passing rates and readability metrics for each iteration will be displayed in a metrics.json file under `data/problems_dir_name/metrics/timestamp_metrics.json` for the timestamp for that run.

# Autoencoder Pipeline
Below is code to run the autoencoder with *Greedy Refinement* agent for LeetCode dataset for 32 iterations.
```python
from agents import GreedyRefine, DirectAnswer, FunSearch, AIDE, ChainOfExperts, ReEvo, BestOfN
from evaluation import Evaluator, get_data

# Set greedy_refine in the cfg file
if cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga

# Select directory name, version, and split
if problems_dir_name == 'leet_code':
    version = 'v0.3.0'
    split = 'train'
    problems_filename = f'LeetCodeDataset-{version}-{split}.jsonl'
    data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')

starting_iteration = 1
iterations = 32
rounds = 2
timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1]

# Set up dataset:
if (evolving_encoding or evolving_decoding or evolving_cosmetic or evolving_classifier) and not load_previous: 
        setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 3) 

# Define agents
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

# Set trivial decoder prompt for encoder to start off with:
prev_decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/common/trivial_decoder_prompt.txt")

# Load evaluator
evaluator = Evaluator(data, timeout=10)

# Run for 32 iterations:
for it in range(starting_iteration, iterations + 1):
    # Encoding:
    if evolving_encoding:
        stage = 'encoder'
        try: 
            prompt = encoding_agent.step()
        
            if prompt is None:  
                break
            feedback = evaluator.evaluate(prompt, prev_decoder_prompt, stage, timestamp, it, client)  # Run evaluation
            avg_metrics = feedback.avg_metrics

            # Save metrics to file for each iteration
            save_metrics(avg_metrics, metrics_path, timestamp, stage, it)

            # Save prompt to file for each iteration
            save_prompt(str(generated_prompts_path), prompt, it, stage)
            
            # UNCOMMENT BELOW:
            encoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback

            # Record previous best prompt
            previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
            previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = encoding_agent.get_previous_best()
            record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)
            
            # Get the final best solution before switching over to decoder
            if it % rounds == 0: 
                best_prompt_so_far = encoding_agent.finalize()
                prev_encoder_prompt = best_prompt_so_far

        except Exception as e:
            print(f"Error in iteration {it} for stage {stage}: {e}")
            traceback.print_exc()
            continue  # Skip to the next round
    if evolving_decoding:
        stage = 'decoder'
        try:
            prompt = decoding_agent.step()
            if prompt is None:  
                break
            feedback = evaluator.evaluate(prompt, prev_encoder_prompt, stage, timestamp, it, client)  # Run evaluation
            avg_metrics = feedback.avg_metrics

            # Save metrics to file for each iteration
            save_metrics(avg_metrics, metrics_path, timestamp, stage, it)

            # Save prompt to file for each iteration
            save_prompt(str(generated_prompts_path), prompt, it, stage)
            
            decoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it) 

            # Record previous best prompt
            previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
            previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = decoding_agent.get_previous_best()
            record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)

            # Get the final best solution before switching over to encoder
            if it % rounds == 0: 
                best_prompt_so_far = decoding_agent.finalize()
                prev_decoder_prompt = best_prompt_so_far

        except Exception as e:
            print(f"Error in iteration {it} for stage {stage}: {e}")
            continue  # Skip to the next round
    # Switch to next stage
    if (evolving_encoding or evolving_decoding) and it % rounds == 0: 
        evolving_encoding = not evolving_encoding
        evolving_decoding = not evolving_decoding

# Finalize: Run encoder and decoder again on their best prompts
if (evolving_encoding or evolving_decoding) and iterations > 1:

    prompt = encoding_agent.finalize()
    save_prompt(str(generated_prompts_path), prompt, iterations + 1, 'encoder')
    feedback = evaluator.evaluate(prompt, prev_decoder_prompt, 'encoder', timestamp, iterations + 1, client)
    avg_metrics = feedback.avg_metrics
    save_metrics(avg_metrics, metrics_path, timestamp, 'encoder', iterations + 1)

    prompt = decoding_agent.finalize()
    save_prompt(str(generated_prompts_path), prompt, iterations + 2, 'decoder')
    feedback = evaluator.evaluate(prompt, prev_encoder_prompt, 'decoder', timestamp, iterations + 2, client)
    avg_metrics = feedback.avg_metrics
    save_metrics(avg_metrics, metrics_path, timestamp, 'decoder', iterations + 2)
```


# Cosmetic Changes Pipeline
Below is code to run the cosmetic changes pipeline with *Greedy Refinement* agent for LeetCode dataset for 32 iterations.

First, we need to get either the positive_labels jsonl file by calling `get_positive_labels(metrics_file, autoencoder_directory_name, jsonl_filename, new_file_name, autoencoder_timestamp)` or the pseucodoe_labels jsonl file by calling `get_pseudocode_labels(metrics_file, first_dir, autoencoder_directory_name, new_file_name, autoencoder_timestamp)`

```python
# Set greedy_refine in the cfg file
if cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga

# Select directory name, previous_timestamp, and either a positive_labels or pseudocode_labels jsonl file
if problems_dir_name = 'cosmetic_pseudocodes:
    previous_timestamp = '2025-09-26_19-55-20'
    # problems_filename = f"positive_labels_{previous_timestamp}.jsonl"
    problems_filename = f"pseudocode_labels_{previous_timestamp}.jsonl"
    data = get_data(problems_dir_name, problems_filename, src_dir=f'{ROOT_DIR}/data')

starting_iteration = 1
cosmetic_iterations = 32
timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1]

# Set up dataset:
if (evolving_encoding or evolving_decoding or evolving_cosmetic or evolving_classifier) and not load_previous: 
        setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 3) 

# Define agents
cosmetic_agent = ga(
    client=client,
    src_dir=ROOT_DIR,
    timeout=5,
    model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
    stage='cosmetic'
)

# Load Evaluator
evaluator = Evaluator(data, timeout=5)

# Set final_iter, previous_timestamp to load in best decoder prompt from the autoencoder pipeline
final_iter = 34
previous_timestamp = '2025-09-18_21-00-18'
decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_decoder_prompt.txt")

# Run for 32 iterations:
for it in range(1, cosmetic_iterations+1):
    if evolving_cosmetic:
        stage = 'cosmetic'
        try: 
            prompt = cosmetic_agent.step()
           
            if prompt is None:  
                break

            feedback = evaluator_cosmetic.evaluate_cosmetic(prompt, decoder_prompt, stage, timestamp, it, client)
            avg_metrics = feedback.avg_metrics

            # Save metrics to file for each iteration
            save_metrics(avg_metrics, metrics_path, timestamp, stage, it)

            # Save prompt to file for each iteration
            save_prompt(str(generated_prompts_path), prompt, it, stage)
            
            cosmetic_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  

            # Record previous best prompt:
            previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
            previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = cosmetic_agent.get_previous_best()
            record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)

            
        except Exception as e:
            print(f"Error in iteration {it} for stage {stage}: {e}")
            continue
```

# Classifier Pipeline
Below is code to run the classifier pipeline with *Greedy Refinement* agent for LeetCode dataset for 32 iterations.

```python
# Set greedy_refine in the cfg file
if cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga

# Select directory name, version, and split
if problems_dir_name = 'classifier_pseudocodes':
    version = 3
    train_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-train.jsonl" )
    dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"HumanEval-pseudo-v0.{version}.0-dev.jsonl")
    classifier_dataset_name = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes")

starting_iteration = 1
classifier_iterations = 32 = 32# [TO DO]: CO-Bench paper uses 64
timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1]

# Set up dataset:
if (evolving_encoding or evolving_decoding or evolving_cosmetic or evolving_classifier) and not load_previous: 
        setup_dataset(timestamp, f"{ROOT_DIR}/data/{problems_dir_name}", iterations + 2) 

# Define agent
classifier_agent = ga(
    client=client,
    src_dir=ROOT_DIR,
    timeout=5,
    model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
    stage='classifier'
)

# Set final_iter, previous_timestamp to load in best decoder prompt from the autoencoder pipeline
final_iter = 34
previous_timestamp = '2025-09-18_21-00-18'
decoder_prompt = file_to_string(f"{ROOT_DIR}/prompts/greedy_refine/trivial_decoder_prompt.txt")

# Run for 32 iterations
for it in range(1, classifier_iterations + 1):
    if evolving_classifier:
        stage = 'classifier'
        try: 
            prompt = classifier_agent.step()
            
            if prompt is None: 
                break
            save_prompt(str(generated_prompts_path), prompt, it, stage)
            
            mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client)
            
            feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)   
            score = feedback.dev_score
        
            classifier_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  

            avg_metrics = feedback.avg_metrics
            save_metrics(avg_metrics, metrics_path, timestamp, stage, it)

            # Record previous best prompt:
            previous_best_path = os.path.join(ROOT_DIR, "data", problems_dir_name, "outputs", timestamp, f"iter_{it}", "previous_best", "previous_best.json")
            previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = classifier_agent.get_previous_best()
            record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)

        except Exception as e:
            print(f"Error in iteration {it} for stage {stage}: {e}")
            continue  

if evolving_classifier:
        # test final classifier prompt with dev_set and test_set
        # UNCOMMENT PROMPT BELOW:
        prompt = classifier_agent.finalize()

        generated_prompts_path = Path(f"{ROOT_DIR}/outputs/prompts/{timestamp}")
        generated_prompts_path.mkdir(parents=True, exist_ok=True)
        save_prompt(str(generated_prompts_path), prompt, classifier_iterations+1, 'classifier')
        save_prompt(str(generated_prompts_path), prompt, classifier_iterations+2, 'classifier')
        # train score:
        mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, labeled_correctly, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(train_set_filename, prompt, client)
        feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  # Run evaluation
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+1)
        pseudocode_path = os.path.join(classifier_dataset_name, "outputs", timestamp, f"iter_{classifier_iterations+1}", "pseudocodes")
        write_classifier_pseudocodes_to_file(labeled_correctly, os.path.join(pseudocode_path, "pass"))
        mislabeled = mislabeled_positives + mislabeled_cosmetic + mislabeled_negatives + mislabeled_near_misses
        write_classifier_pseudocodes_to_file(mislabeled, os.path.join(pseudocode_path, "fail"))
        # val score:
        dev_set_filename = os.path.join(ROOT_DIR, "data", "classifier_pseudocodes", f"LeetCode-pseudo-v0.{version}.0-dev.jsonl" )
        mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, labeled_correctly, true_negative_errors, near_miss_errors, final_score, metrics = evaluate_classifier_prompt(dev_set_filename, prompt, client)
        dev_feedback = evaluator_classifier.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics)  
        avg_metrics = dev_feedback.avg_metrics
        save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+2)

        pseudocode_path = os.path.join(classifier_dataset_name, "outputs", timestamp, f"iter_{classifier_iterations+2}", "pseudocodes")
        write_classifier_pseudocodes_to_file(labeled_correctly, os.path.join(pseudocode_path, "pass"))
        mislabeled = mislabeled_positives + mislabeled_cosmetic + mislabeled_negatives + mislabeled_near_misses
        write_classifier_pseudocodes_to_file(mislabeled, os.path.join(pseudocode_path, "fail"))
        # test score:
        mislabeled_positives, mislabeled_negatives, labeled_correctly, avg_metrics = evaluate_classifier_prompt_test(test_set_filename, prompt, client)
        save_metrics(avg_metrics, metrics_path, timestamp, "classifier", classifier_iterations+3)
        pseudocode_path = os.path.join(classifier_dataset_name, "outputs", timestamp, f"iter_{classifier_iterations+3}", "pseudocodes")
        write_classifier_pseudocodes_to_file(labeled_correctly, os.path.join(pseudocode_path, "pass"))
        mislabeled = mislabeled_positives + mislabeled_negatives
        write_classifier_pseudocodes_to_file(mislabeled, os.path.join(pseudocode_path, "fail"))

```

