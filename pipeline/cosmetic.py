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


class Cosmetic(BasePipeline):
    def __str__(self):
        return f"BasePipeline"

    def __init__(self, client, src_dir, cfg, agent, evaluator, timestamp, split, timeout=10, model='openai/o3-mini', max_iter=64, reasoning_effort='medium'):
        self.client=client
        self.src_dir=src_dir
        self.cfg=cfg
        self.agent=agent
        self.evaluator=evaluator
        self.timestamp=timestamp
        self.split=split
        self.timeout = timeout
        self.model = model
        self.stage = 'cosmetic'
        self.max_iter = max_iter
        self.reasoning_effort = reasoning_effort
        self.iteration = 0
        self.pipeline_name = 'cosmetic'

        self.setup_pipeline()

    def setup_pipeline(self):
        generated_prompts_path_timestamp = Path(os.path.join(self.src_dir, "outputs", "prompts", self.timestamp))
        generated_prompts_path_timestamp.mkdir(parents=True, exist_ok=True)

        generated_prompts_path_general = Path(os.path.join(self.src_dir, "outputs", "prompts", f"cosmetic_{self.split}"))
        generated_prompts_path_general.mkdir(parents=True, exist_ok=True)

        self.generated_prompts_path_timestamp = str(generated_prompts_path_timestamp)
        self.generated_prompts_path_general = str(generated_prompts_path_general)

        # [TO DO]: modify the data folder to have human_eval and leet_code folders for the cosmetic folder
        metrics_path = os.path.join(self.src_dir, "data", self.pipeline_name, self.cfg.dataset, "metrics") # TO DO: fill in the variable names
        self.metrics_path = metrics_path

        # [ TO DO]: finish the following refactoring:
        # [TO DO]: check that the decoder prompt actually was written to a special outputs foldeer
        if self.cfg.use_timestamp:
            if self.cfg.prev_iter_decoder is not None and self.cfg.previous_autoencoder_label is not None:
                self.decoder_prompt = file_to_string(os.path.join(self.src_dir, "outputs", "prompts", self.cfg.previous_cosmetic_label, f"prompt_iter_{self.cfg.prev_iter_decoder}_decoder.txt"))
            else:
                self.decoder_prompt = file_to_string(os.path.join(self.src_dir, "prompts", "common", "trivial_decoder_prompt.txt"))
        else:
            self.decoder_prompt = file_to_string(os.path.join(self.src_dir, "outputs", "prompts", f"autoencoder_{self.split}", f"prompt_iter_{self.cfg.num_iterations + 2}_decoder.txt"))


        if self.cfg.load_previous:
            self.load_previous_state()

    def load_previous_state(self):
        previous_best_path = os.path.join(self.src_dir, "data", self.pipeline_name, self.cfg.dataset, "outputs", self.cfg.load_previous_timestamp, f"iter_{self.cfg.previous_last_iter}", "previous_best", "previous_best.json")
        self.agent.load_previous(previous_best_path)

    def run(self):
        for it in range(self.cfg.starting_iteration, self.cfg.num_iterations + 1):
            try: 
                prompt = self.agent.step()

                if prompt is None:  
                    break
                feedback = self.evaluator.evaluate_cosmetic(prompt, self.decoder_prompt, self.stage, self.timestamp, it, self.client, self.split, self.cfg.near_miss_threshold)

                self._save_iteration_results(feedback.avg_metrics, prompt, it)
                
                self.agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback
                # Record Previous best:
                self._record_previous_best(self.agent, it)
                              
            except Exception as e:
                print(f"Error in iteration {it} for stage {self.stage}: {e}")
                traceback.print_exc()
                continue 
        

    def _save_iteration_results(self, avg_metrics, prompt, it):
        save_metrics(avg_metrics, self.metrics_path, self.timestamp, self.stage, it, self.split)
        save_prompt(self.generated_prompts_path_timestamp, prompt, it, self.stage) 
        save_prompt(self.generated_prompts_path_general, prompt, it, self.stage)

    def _record_previous_best(self, agent, it):
        # [TO DO]: incorporate split and use_timestamp into record_previous_best
        previous_best_path = os.path.join(self.src_dir, "data", self.pipeline_name, self.cfg.dataset, "outputs", self.timestamp, f"iter_{it}", "previous_best", "previous_best.json")
        previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = agent.get_previous_best()
        record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)
                

    