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
from utils.utils import init_client, file_to_string, set_up_dataset, preprocess_data, plot_pipeline, set_up_dataset, set_up_codebase
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

    # Uncomment below when first setting up
    # set_up_codebase(ROOT_DIR)
    # preprocess_data(ROOT_DIR) 
    
    # Main algorithm

    timestamp = hydra.core.hydra_config.HydraConfig.get().run.dir.split("/")[-1] # this should syncronize with hydra's timestamp

    # Run all 3 pipelines one after the other

    if not cfg.use_timestamp:
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

    if cfg.evolving_cosmetic and cfg.use_timestamp:
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

    if cfg.evolving_classifier and cfg.use_timestamp:
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



if __name__ == "__main__":
    main()