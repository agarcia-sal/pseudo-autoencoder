import os
import traceback
from pathlib import Path
from evaluation.utils import save_metrics, save_prompt, record_previous_best_solution, file_to_string
from .base_pipeline import BasePipeline


# @dataclass
# class Solution:
#     prompt: str
#     score: Optional[float] = None
#     feedback: Optional[str] = None
#     response: Optional[str] = None
#     iter: Optional[float] = None


class AutoEncoder(BasePipeline):
    def __str__(self):
        return f"BasePipeline"

    def __init__(self, client, src_dir, cfg, encoding_agent, decoding_agent, evaluator, timestamp, timeout=10, model='openai/o3-mini', stage='encoder', max_iter=64, reasoning_effort='medium'):
        self.client=client
        self.src_dir=src_dir
        self.cfg = cfg
        self.encoding_agent = encoding_agent
        self.decoding_agent = decoding_agent
        self.evaluator = evaluator
        self.timestamp = timestamp
        self.timeout = timeout
        self.model = model
        self.stage = stage
        self.max_iter = max_iter
        self.reasoning_effort = reasoning_effort
        self.iteration = 0
        self.pipeline_name = 'autoencoder'

        self.setup_pipeline()

    def setup_pipeline(self):
        generated_prompts_path = Path(os.path.join(self.src_dir, "outputs", "prompts", self.timestamp))
        generated_prompts_path.mkdir(parents=True, exist_ok=True)
        self.generated_prompts_path = str(generated_prompts_path)

        metrics_path = os.path.join(self.src_dir, "data", self.pipeline_name, self.cfg.dataset, "metrics") # TO DO: fill in the variable names
        self.metrics_path = metrics_path

        self.prev_decoder_prompt = file_to_string(os.path.join(self.src_dir, "prompts", "common", "trivial_decoder_prompt.txt"))
        self.prev_encoder_prompt = file_to_string(os.path.join(self.src_dir, "prompts", "common", "trivial_encoder_prompt.txt"))
        
        self.evolving_encoding = self.cfg.evolving_encoding # set to True if i want to run setup_pipeline
        self.evolving_decoding = self.cfg.evolving_decoding
        

    def run(self):
        for it in range(self.cfg.starting_iteration, self.cfg.num_iterations + 1):
            if self.evolving_encoding:
                # stage = 'encoder'
                try: 
                    prompt = self.encoding_agent.step() # [TO DO]: pass in the encoding_agent
                    
                    if prompt is None: 
                        break

                    # pass in the evaluator
                    feedback = self.evaluator.evaluate(prompt, self.prev_decoder_prompt, self.stage, self.timestamp, it, self.client)  

                    self._save_iteration_results(feedback.avg_metrics, prompt, it)
                    
                    self.encoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback

                    self._record_previous_best(self.encoding_agent, it)

                    # Get the final solution
                    if it % self.cfg.rounds == 0: # about to switch over to the next stage
                        best_prompt_so_far = self.encoding_agent.finalize()
                        self.prev_encoder_prompt = best_prompt_so_far

                except Exception as e:
                    print(f"Error in iteration {it} for stage {self.stage}: {e}")
                    traceback.print_exc()
                    continue  

            if self.evolving_decoding:
                # stage = 'decoder'
                try:
                    prompt = self.decoding_agent.step()
                    if prompt is None: 
                        break 
                    feedback = self.evaluator.evaluate(prompt, self.prev_encoder_prompt, self.stage, self.timestamp, it, self.client)  
                    
                    self._save_iteration_results(feedback.avg_metrics, prompt, it)
                    
                    self.decoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback

                    # Record Previous best
                    self._record_previous_best(self.decoding_agent, it)

                    # Get the final solution
                    if it % self.cfg.rounds == 0: # about to switch over to the next stage
                        best_prompt_so_far = self.decoding_agent.finalize()
                        self.prev_decoder_prompt = best_prompt_so_far

                except Exception as e:
                    print(f"Error in iteration {it} for stage {self.stage}: {e}")
                    continue  

            if it % self.cfg.rounds == 0: 
                if self.stage == 'encoder':
                    self.stage = 'decoder'
                else:
                    self.stage = 'decoder'
                self.evolving_encoding = not self.evolving_encoding
                self.evolving_decoding = not self.evolving_decoding
            

    def finalize(self):
        # Encoding
        prompt = self.encoding_agent.finalize()
        save_prompt(self.generated_prompts_path, prompt, self.cfg.num_iterations + 1, 'encoder')
        feedback = self.evaluator.evaluate(prompt, self.prev_decoder_prompt, 'encoder', self.timestamp, self.cfg.num_iterations + 1, self.client)
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, self.metrics_path, self.timestamp, 'encoder', self.cfg.num_iterations + 1)
        print('encoding prompt:')
        print(prompt)
        
        # Decoding
        prompt = self.decoding_agent.finalize()
        save_prompt(self.generated_prompts_path, prompt, self.cfg.num_iterations + 2, 'decoder')
        feedback = self.evaluator.evaluate(prompt, self.prev_encoder_prompt, 'decoder', self.timestamp, self.cfg.num_iterations + 2, self.client)
        avg_metrics = feedback.avg_metrics
        save_metrics(avg_metrics, self.metrics_path, self.timestamp, 'decoder', self.cfg.num_iterations + 2)
        print('decoding prompt:')
        print(prompt)


    def _save_iteration_results(self, avg_metrics, prompt, it):
        save_metrics(avg_metrics, self.metrics_path, self.timestamp, self.stage, it) 
        save_prompt(self.generated_prompts_path, prompt, it, self.stage) 

    def _record_previous_best(self, agent, it):
        previous_best_path = os.path.join(self.src_dir, "data", self.pipeline_name, self.cfg.dataset, "outputs", self.timestamp, f"iter_{it}", "previous_best", "previous_best.json")
        previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = agent.get_previous_best()
        record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)
                

    