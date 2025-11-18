# Pseudo-Autoencoder: Large Language Models for Examining Pseudocode Validity

**Data:** [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset) and [HumanEval](https://github.com/openai/human-eval)

# Download Data
Download the raw data from [HumanEval](https://github.com/openai/human-eval) to the local directory `data/autoencoder/human_eval` and LeetCodeDataset-v0.3.0-train.jsonl and LeetCodeDataset-v0.3.0-test.jsonl from [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset) to the local directory `data/autoencoder/leet_code`

# Set Up Environment - Usage

- Set your OpenAI API key as an environment variable:
    ```bash
    OPENAI_API_KEY="<Your API key>" # see more options in ./cfg/llm_client
    ```

When first running the code, uncomment the line below in the main function:
```python
# uncomment below when first setting up
# preprocess_data(ROOT_DIR) 
```
The `preprocess_data` function will do reformat the HumanEval dataset as well as create a new version of the LeetCodeDataset-v0.3.0 that will be which will be a 50% split of medium difficulty and 50% split of hard difficulty instead of a mix of 'easy', 'medium', and 'hard'. The new version of the dataset will be called LeetCodeDataset-v0.3.5-train.jsonl and LeetCodeDataset-v0.3.5-test.jsonl

# Agent Implementations

Agents are implemented in the `agents` module. Currently supported agents include: `GreedyRefine`, `DirectAnswer`

in the cfg/config.yaml file, set `algorithm` to `greedy` or `direct_answer`, depending on which one you're using.

Each agent implements the following functions:
- `step()`: Returns the next candidate prompt for evaluation.
- `feedback()`: Accepts evaluation results of previous candidate prompt and returns feedback for LLM prompt.
- `finalize()`: Returns the final prompt.
- `get_previous_best()`: Returns previous best Solution so far to store at each iteration of a pipeline
- `load_previous()`: If a pipeline stops running prematurely, will return previous best solution up to that point so that the pipeline can continue running

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

# Pipeline selection

There are 3 pipelines available to run: Autoencoder, Cosmetic, and Classifier

In the cfg/config.yaml file Set the `evolving_encoder`, `evolving_decoder`, `evolving_cosmetic`, `evolving_classifier` flag to True depending on which pipeline you want to run. For the autoencoder pipeline, set the `evolving_encoder` flag to True and `evolving_decoder` flag to False to start off with. The flags will toggle as the autoencoder switches between these two stages.

Also in the cfg/config.yaml file, set `pipeline` to either `autoencoder`, `cosmetic`, `classifier` and specify which dataset you are using by setting `dataset` to either `human_eval` or `leet_code`. Set `num_iterations` to however many iterations you want to run. Default is 32. Set `rounds`, which is the number of iterations run before switching from encoder to decoder and vice versa. Default is 2.

# Workflow

The autoencoder pipeline can be run separately but to run the cosmetic pipeline, first run the autoencoder pipeline. To run the classifier pipeline, run the autoencoder pipeline and then the cosmetic pipeline. Each run of each pipeline will have a timestamp associated with it. The entire workflow with all the pipelines is as follows: 
1. Run the autoencoder on the training set to generate the pseudocodes with their labels
    - the end result is a folder named by the timestamp with all the pseudocodes and codes generated per iteration
2. Run the autoencoder on the testing set to generate the pseudocodes with their labels
3. Call get_cosmetic_dataset() to get AutoEncoderLabels_{cosmetic_version}-train.jsonl, which is generated from the pseudocodes generated by the autoencoder 
4. Call get_cosmetic_dataset() to get AutoEncoderLabels_{cosmetic_version}-test.jsonl
5. Run the cosmetic pipeline on AutoEncoderLabels_{cosmetic_version}-train.jsonl
6. Run the cosmetic pipeline on AutoEncoderLabels_{cosmetic_version}-test.jsonl
7. Call get_classifier_dataset() with the autoencoder and cosmetic timestamps set in cfg to create HumanEvalPseudocodes-{classifier_version}-train.jsonl or LeetCodePseudocodes-{classifier_version}-train.jsonl
8. Call get_classifier_dataset() with the autoencoder and cosmetic timestamps set in cfg to create HumanEvalPseudocodes-{classifier_version}-test.jsonl or LeetCodePseudocodes-{classifier_version}-test.jsonl
9. Run the classifier pipeline

# Results

Passing rates and readability metrics for each iteration will be displayed in a metrics.json file under `data/pipeline/dataset/metrics/timestamp_metrics.json` for the timestamp for that run.

# Autoencoder Pipeline

In the cfg/config.yaml file, set the following values:
- `split` to either `train` or `test`
- `autoencoder_version` to whichever version of the LeetCodeDataset is being used, if `leet_code` is the chosen dataset. Default is `v0.3.5` which is the more difficult version of `v0.3.0`

Below is code to run the autoencoder with *Greedy Refinement* agent for LeetCode dataset for 32 iterations. If running *Direct Answer* then pass in the timestamp for the decoder prompt generated by the autoencoder pipeline that should be used.
```python
from agents import GreedyRefine, DirectAnswer
from evaluation import Evaluator, get_data

# Set greedy_refine in the cfg file
if cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga

timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp

if (cfg.evolving_encoder or cfg.evolving_decoder or cfg.evolving_cosmetic or cfg.evolving_classifier) and not cfg.load_previous: 
    setup_dataset(timestamp, os.path.join(ROOT_DIR, "data", cfg.pipeline, cfg.dataset), cfg.num_iterations + 3) # plus 2 because of the final encoder and decoder verification at the end with train, val, and test splits


if cfg.evolving_encoder or cfg.evolving_decoder:
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

    data = get_data(cfg, src_dir=os.path.join(ROOT_DIR, "data", cfg.pipeline))

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
```


# Cosmetic Changes Pipeline
First, call `get_cosmetic_dataset()` to get the AutoEncoderLabels-{cfg.cosmetic_version}-{cfg.split}.jsonl that the cosmetic pipeline will use to run.

In the cfg/config.yaml file, set the following values:
- `cosmetic_version` to whichever version of the AutoEncoderLabels dataset the cosmetic pipeline will use. Should generally increment by 1 e.g `v0.1.0` to `v0.2.0`
- `split` to either `train` or `test` depending on which split the autoencoder used.
- `autoencoder_timestamp` to the timestamp of the autoencoder run that the cosmetic pipeline is building off of

Below is code to run the cosmetic changes pipeline with *Greedy Refinement* agent for LeetCode dataset for 32 iterations.

```python
from agents import GreedyRefine, DirectAnswer
from evaluation import Evaluator, get_data

# Set greedy_refine in the cfg file
if cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga

timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp

if (cfg.evolving_encoder or cfg.evolving_decoder or cfg.evolving_cosmetic or cfg.evolving_classifier) and not cfg.load_previous: 
    setup_dataset(timestamp, os.path.join(ROOT_DIR, "data", cfg.pipeline, cfg.dataset), cfg.num_iterations + 3) # plus 2 because of the final encoder and decoder verification at the end with train, val, and test splits

if cfg.evolving_cosmetic:
    cosmetic_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
        stage='cosmetic'
    )

    get_cosmetic_dataset(cfg)
    data = get_data(cfg, src_dir=os.path.join(ROOT_DIR, "data", cfg.pipeline))
    evaluator_cosmetic = Evaluator(data, timeout=5) 

    cosmetic = Cosmetic(
        client=client, 
        src_dir=ROOT_DIR, 
        cfg=cfg,
        agent=cosmetic_agent, 
        evaluator=evaluator_cosmetic,
        timestamp=timestamp,
        final_iter=34,
        previous_timestamp=cfg.autoencoder_timestamp,
        timeout=5, 
        model='gpt-4.1-mini',         
    )

    cosmetic.run()
```

# Classifier Pipeline
In the cfg/config.yaml file, set the following values:
- `classifier_version` to whichever version of the HumanEvalPseudocodes or LeetCodePseudocodes dataset the classifier pipeline will use. Should generally increment by 1 e.g `v0.1.0` to `v0.2.0`
- `split` to `train`
- `autoencoder_timestamp_train` to the timestamp of the autoencoder run for the train split that `get_classifier_dataset()` will use to create the classifier dataset
- `cosmetic_timestamp_train` to the timestamp of the cosmetic run for the train split that `get_classifier_dataset()` will use to create the classifier dataset
- `autoencoder_timestamp_test` to the timestamp of the autoencoder run for the test split that `get_classifier_dataset()` will use to create the classifier dataset
- `cosmetic_timestamp_test` to the timestamp of the cosmetic run for the test split that `get_classifier_dataset()` will use to create the classifier dataset

Then, call `get_classifier_dataset(split='train')` to get the Pseudocodes-{cfg.classifier_version}-train.jsonl that the classifier pipeline will use to run. Call `get_classifier_dataset(split='test')` to get the Pseudocodes-{cfg.classifier_version}-test.jsonl that the classifier pipeline will use to score final results.

Below is code to run the classifier pipeline with *Greedy Refinement* agent for LeetCode dataset for 32 iterations.

```python
from agents import GreedyRefine, DirectAnswer
from evaluation import Evaluator, get_data

# Set greedy_refine in the cfg file
if cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga

timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp

if (cfg.evolving_encoder or cfg.evolving_decoder or cfg.evolving_cosmetic or cfg.evolving_classifier) and not cfg.load_previous: 
    setup_dataset(timestamp, os.path.join(ROOT_DIR, "data", cfg.pipeline, cfg.dataset), cfg.num_iterations + 3) # plus 2 because of the final encoder and decoder verification at the end with train, val, and test splits

if cfg.evolving_classifier:
    classifier_agent = ga(
        client=client,
        src_dir=ROOT_DIR,
        timeout=5,
        model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM ap
    )

    get_classifier_dataset(cfg, split='train', limit=150)
    get_classifier_dataset(cfg, split='test', limit=150)
    data = get_data(cfg, src_dir=os.path.join(ROOT_DIR, "data", cfg.pipeline))
    evaluator_classifier = Evaluator(data, timeout=5) 

    classifier = Classifier(
        client=client, 
        src_dir=ROOT_DIR, 
        cfg=cfg,
        agent=classifier_agent, 
        evaluator=evaluator_classifier,
        timestamp=timestamp,
        final_iter=34,
        previous_timestamp=cfg.autoencoder_timestamp,
        timeout=5, 
        model='gpt-4.1-mini',         
    )

    classifier.run()
    classifier.finalize()
```

