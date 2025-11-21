# Pseudo-Autoencoder: Large Language Models for Examining Pseudocode Validity

**Data:** [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset) and [HumanEval](https://github.com/openai/human-eval)

# Download Data

When first running the code, uncomment the line below in the main function:

```python
# uncomment below when first setting up
# set_up_codebase(ROOT_DIR)
```
The `set_up_codebase` function will set up necessary folder structure.

Download the raw data from [HumanEval](https://github.com/openai/human-eval) to the local directory `data/autoencoder/human_eval` and LeetCodeDataset-v0.3.0-train.jsonl and LeetCodeDataset-v0.3.0-test.jsonl from [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset) to the local directory `data/autoencoder/leet_code`

# Usage

Set your OpenAI API key as an environment variable:
```bash
OPENAI_API_KEY="<Your API key>" # see more options in ./cfg/llm_client
```

Create a new conda environment with the pseudo_env.yml file:
```bash
conda env create -f pseudo_env.yml
```

When first running the code, uncomment the line below in the main function:
```python
# uncomment below when first setting up
# preprocess_data(ROOT_DIR) 
```

The `preprocess_data` function will do reformat the HumanEval dataset as well as create a new, shorter version of the LeetCodeDataset-v0.3.0 that will be which will be a 50% split of medium difficulty and 50% split of hard difficulty instead of a mix of 'easy', 'medium', and 'hard'. The new version of the dataset will be called LeetCodeDataset-v0.3.5-train.jsonl and LeetCodeDataset-v0.3.5-test.jsonl

# Agent Implementations

Agents are implemented in the `agents` module. Currently supported agents include: `GreedyRefine`, `DirectAnswer`

in the cfg/config.yaml file, set `algorithm` to `greedy` or `direct_answer`, depending on which one you're using.

Each agent implements the following functions:
- `step()`: Returns the next candidate prompt for evaluation.
- `feedback()`: Accepts evaluation results of previous candidate prompt and returns feedback for LLM prompt.
- `finalize()`: Returns the final prompt.
- `get_previous_best()`: Returns previous best Solution so far to store at each iteration of a pipeline
- `load_previous()`: If a pipeline stops running prematurely, will return previous best solution up to that point so that the pipeline can continue running

# Pipeline selection

There are 3 pipelines available to run: Autoencoder, Cosmetic, and Classifier. They can be run separately by loading in the timestamps of the previous pipeline or they can be run all at once. To run them individually:

In the cfg/config.yaml file Set the `evolving_encoder`, `evolving_decoder`, `evolving_cosmetic`, `evolving_classifier` flag to True depending on which pipeline you want to run. For the autoencoder pipeline, set the `evolving_encoder` flag to True and `evolving_decoder` flag to False to start off with. The flags will toggle as the autoencoder switches between these two stages.

Also in the cfg/config.yaml file, set `pipeline` to either `autoencoder`, `cosmetic`, `classifier` and specify which dataset you are using by setting `dataset` to either `human_eval` or `leet_code`. Set `num_iterations` to however many iterations you want to run. Default is 32. Set `rounds`, which is the number of iterations run before switching from encoder to decoder and vice versa. Default is 2.

Further, in the cfg/config.yaml file, set `autoencoder_version`, `cosmetic_version`, `classifier_version`. The `autoencoder_version` is the version of the LeetCodeDataset that will be used to start off with. The dataset that the cosmetic pipeline will use will be created throughout the workflow and the version name corresponds to the value set for `cosmetic_version`. The dataset that the classifier pipeline will use will also be created throughout the worfklow and the version name corresponds to the value set for `classifier_version`.

# Workflow for sequential run of the 3 pipelines
To run the entire workflow at once, set the following values in the config.yaml file:
- `dataset`: `leet_code` or `human_eval`
- `use_timestamp`: `False` # if running pipelines individually, set to True
- `num_iterations`: the number of iterations for a pipeline. Default is 32
- `rounds`: 2 
- `evolving_encoder`: True
- `autoencoder_version`: the version of the LeetCodeDataset being used. Default is v0.3.5 which is the harder version of v0.3.0
- `cosmetic_version`: v0.1.0 # update this as more datasets for the cosmetic pipeline are created
- `classifier_version`: v0.1.0
- `readability_metric`: `avg_syllables_per_word` or `avg_word_length`. Default is `avg_syllables_per_word`    
- `near_miss_threshold`: 0.8

Below is the code to run the entire worfklow at once:

```python
from agents import GreedyRefine, DirectAnswer
from pipeline.experiment_runner import ExperimentRunner

# Set greedy_refine in the cfg file
client = init_client(cfg)

if cfg.algorithm == "reevo":
    from reevo import ReEvo as ga
elif cfg.algorithm == "greedy":
    from agents.greedy_refine import GreedyRefine as ga
elif cfg.algorithm == "direct_answer":
    from agents.direct_answer import DirectAnswer as ga
else:
    raise NotImplementedError

# Uncomment below when first setting up
# preprocess_data(ROOT_DIR) 
# set_up_codebase(ROOT_DIR)

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
```

# Results

Passing rates and readability metrics for each iteration will be displayed in a metrics.json file under `data/pipeline/dataset/metrics/timestamp_metrics.json` for the timestamp for that run.

To plot pipelines after individual runs, set the values for the timestamps of those runs:
```python
if cfg.plotting_pipeline:
    autoencoder_timestamp = '2025-11-18_14-39-59'
    classifier_timestamp = '2025-11-18_19-27-00'
    if not cfg.use_timestamp:
        autoencoder_timestamp = timestamp
        classifier_timestamp = timestamp
    plot_pipeline(cfg, ROOT_DIR, autoencoder_timestamp, "autoencoder")
    plot_pipeline(cfg, ROOT_DIR, classifier_timestamp, "classifier")
    plt.show()
```

# Autoencoder Pipeline

In the cfg/config.yaml file, set the following values:
- `split` to either `train` or `test`
- `autoencoder_version` to whichever version of the LeetCodeDataset is being used, if `leet_code` is the chosen dataset. Default is `v0.3.5` which is the shorter, more difficult version of `v0.3.0`
- `readability_metric` to either `avg_syllables_per_word` or `avg_word_length`. Default is `avg_syllables_per_word`

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
- `autoencoder_timestamp_train` or `autoencoder_timestamp_test` to the timestamp of the autoencoder run that the cosmetic pipeline is building off of for either the train or test split
- `previous_timestamp_cosmetic` to the timestamp of the autoencoder run from which to load in the decoder prompt from
- `prev_iter_cosmetic` to the iteration of the autoencoder from which to load in the decoder prompt fromn 

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
- `previous_timestamp_classifier` to the timestamp of the autoencoder from which to load in the decoder prompt from
- `prev_iter_classifier` to the iteration of the autoencoder from which to load in the decoder prompt from

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
        model='gpt-4.1-mini',
        stage='classifier',
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
        timeout=5, 
        model='gpt-4.1-mini',         
    )

    classifier.run()
    classifier.finalize()
```

