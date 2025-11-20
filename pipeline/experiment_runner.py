import os
import shutil
from utils.utils import empty_folder, delete_file, set_up_dataset
from evaluation.utils import get_cosmetic_dataset, get_classifier_dataset
from evaluation import Evaluator, get_data

from .autoencoder import AutoEncoder
from .cosmetic import Cosmetic
from .classifier import Classifier

class ExperimentRunner:
    def __init__(self, client, src_dir, cfg, timestamp, ga):
        self.client=client
        self.src_dir=src_dir
        self.cfg=cfg
        self.timestamp=timestamp
        self.ga=ga
        self.pipeline = ''
        # self.state_machine = EvolutionStateMachine(
        #     starting_iteration=config.starting_iteration,
        #     rounds=config.rounds,
        #     initial_stage=EvolutionStage.ENCODING
        # )

    def _set_up_pipeline(self):
        outputs_folder = os.path.join(self.src_dir, "data", self.pipeline, self.cfg.dataset, "outputs", "train")
        empty_folder(outputs_folder)
        metrics_file = os.path.join(self.src_dir, "data", self.pipeline, self.cfg.dataset, "metrics", "train_metrics.json")
        delete_file(metrics_file)

        outputs_folder = os.path.join(self.src_dir, "data", self.pipeline, self.cfg.dataset, "outputs", "test")
        empty_folder(outputs_folder)
        metrics_file = os.path.join(self.src_dir, "data", self.pipeline, self.cfg.dataset, "metrics", "test_metrics.json")
        delete_file(metrics_file)
        set_up_dataset(self.timestamp, os.path.join(self.src_dir, "data", self.pipeline, self.cfg.dataset), self.cfg.num_iterations + 3)
    
    def run_main_evolution(self):
        """Run main evolution with automatic stage switching"""
        
        self.pipeline = 'autoencoder'
        self._set_up_pipeline()
        self._run_autoencoder(split='train')
        self._run_autoencoder(split='test')

        self.pipeline = 'cosmetic'
        self._set_up_pipeline()
        # [TO DO]: change timestamp loading for get_cosmetic_dataset - DONE
        self._run_cosmetic(split='train')
        self._run_cosmetic(split='test')

        self.pipeline = 'classifier'
        self._set_up_pipeline()
        # [TO DO]: change timestamp loading for get_classifier_dataset - DONE
        self._run_classifier()
        
    def _run_autoencoder(self, split='train'):
        # [TO DO]: add a case for using DirectAnswer as the agent framework for autoencoder, cosmetic, classifier pipelines
        

        encoding_agent = self.ga(
            client=self.client,
            src_dir=self.src_dir,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
            stage='encoder',
        )

        if self.cfg.algorithm == 'direct_answer':
            encoding_agent.set_prompt()

        decoding_agent = self.ga(
            client=self.client,
            src_dir=self.src_dir,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
            stage='decoder',
        )

        if self.cfg.algorithm == 'direct_answer':
            decoding_agent.set_prompt()

        data = get_data(self.cfg, os.path.join(self.src_dir, "data"), self.pipeline, split)

        evaluator = Evaluator(data, timeout=5) # [TO DO]: change timeout

        autoencoder = AutoEncoder(
            client=self.client, 
            src_dir=self.src_dir, 
            cfg=self.cfg,
            encoding_agent=encoding_agent, 
            decoding_agent=decoding_agent, 
            evaluator=evaluator,
            timestamp=self.timestamp,
            split=split,
            timeout=5, 
            model='gpt-4.1-mini', 
            stage='encoder', 
        )

        autoencoder.run()
        autoencoder.finalize()

    def _run_cosmetic(self, split='train'):

        cosmetic_agent = self.ga(
            client=self.client,
            src_dir=self.src_dir,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM api
            stage='cosmetic'
        )

        if self.cfg.algorithm == 'direct_answer':
            cosmetic_agent.set_prompt()

        get_cosmetic_dataset(self.cfg, self.src_dir, split)
        data = get_data(self.cfg, os.path.join(self.src_dir, "data"), self.pipeline, split)
        evaluator_cosmetic = Evaluator(data, timeout=5) 

        cosmetic = Cosmetic(
            client=self.client, 
            src_dir=self.src_dir, 
            cfg=self.cfg,
            agent=cosmetic_agent, 
            evaluator=evaluator_cosmetic,
            timestamp=self.timestamp,
            split=split,
            timeout=5, 
            model='gpt-4.1-mini',         
        )

        cosmetic.run()

    def _run_classifier(self, split='train'):
        classifier_agent = self.ga(
            client=self.client,
            src_dir=self.src_dir,
            timeout=5,
            model='gpt-4.1-mini', # We use LiteLLM to call API; was previously 'openai/o3-mini'; im assuming to fit in with LiteLLM ap
            stage='classifier',
        )

        if self.cfg.algorithm == 'direct_answer':
            classifier_agent.set_prompt()

        get_classifier_dataset(self.cfg, self.src_dir, split='train', limit=150)
        get_classifier_dataset(self.cfg, self.src_dir, split='test', limit=150)
        data = get_data(self.cfg, os.path.join(self.src_dir, "data"), self.pipeline, split)
        evaluator_classifier = Evaluator(data, timeout=5) 

        classifier = Classifier(
            client=self.client, 
            src_dir=self.src_dir, 
            cfg=self.cfg,
            agent=classifier_agent, 
            evaluator=evaluator_classifier,
            timestamp=self.timestamp,
            split=split,
            timeout=5, 
            model='gpt-4.1-mini',         
        )

        classifier.run()
        classifier.finalize()