import os
from .base_pipeline import BasePipeline


# @dataclass
# class Solution:
#     prompt: str
#     score: Optional[float] = None
#     feedback: Optional[str] = None
#     response: Optional[str] = None
#     iter: Optional[float] = None


class Classifier(BasePipeline):
    def __str__(self):
        return f"BasePipeline"

    def __init__(self, client, src_dir, timeout=10, model='openai/o3-mini', stage='encoder', max_iter=64, reasoning_effort='medium'):
        self.client=client
        self.src_dir=src_dir
        self.timeout = timeout
        self.model = model
        self.stage = stage
        self.solution = []
        self.max_iter = max_iter
        self.reasoning_effort = reasoning_effort
        self.iteration = 0

        # started adding here:
        self.timestamp = timestamp

        self.setup_pipeline()

    def setup_pipeline(self):
        generated_prompts_path = Path(os.path.join(self.src_dir, "outputs", "prompts", self.timestamp))
        generated_prompts_path.mkdir(parents=True, exist_ok=True)
        self.generated_prompts_path = str(generated_prompts_path)

        metrics_path = os.path.join(self.src_dir, "data", pipeline_name, dataset, "metrics") # TO DO: fill in the variable names
        self.metrics_path = metrics_path

        

    def run(self):
        stage = 'encoder'
            try: 
                prompt = encoding_agent.step()
                
                if prompt is None: 
                    break

                feedback = evaluator.evaluate(prompt, prev_decoder_prompt, stage, timestamp, it, client)  # Run evaluation

                self._save_iteration_results(feedback.avg_metrics, prompt, it)
                
                
                encoding_agent.feedback(feedback.dev_score, feedback.dev_feedback, it)  # Use dev set score as feedback

                self._record_previous_best(encoding_agent, it)
                
                # Get the final solution
                if it % rounds == 0: # about to switch over to the next stage
                    best_prompt_so_far = encoding_agent.finalize()
                    prev_encoder_prompt = best_prompt_so_far

            except Exception as e:
                print(f"Error in iteration {it} for stage {stage}: {e}")
                traceback.print_exc()
                continue  # Skip to the next round
        

    def finalize(self):
        # print('len self.solution in finalize()')
        # print(len(self.solution))
        previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
        # if self.stage == 'decoder':
        #     previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
        # else:
        #     previous_best = sorted(self.solution, key=lambda x: x.score)[0]
        return previous_best.prompt

    def _save_iteration_results(self, avg_metrics, prompt, it):
        save_metrics(avg_metrics, self.metrics_path, self.timestamp, self.stage, it) # [TO DO]: import save_metrics and maybe change self.stage
        save_prompt(self.generated_prompts_path, prompt, it, self.stage) # [TO DO]: import save_prompt and maybe change self.stage

    def _record_previous_best(self, agent, it):
        # [TO DO]: fill in pipeline_name and dataset
        previous_best_path = os.path.join(self.src_dir, "data", pipeline_name, dataset, "outputs", self.timestamp, f"iter_{it}", "previous_best", "previous_best.json")
        previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter = agent.get_previous_best()
        # [TO DO]: import record_previous_best_solution:
        record_previous_best_solution(previous_best_path, previous_best_prompt, previous_best_score, previous_best_feedback, previous_best_iter)
                

    