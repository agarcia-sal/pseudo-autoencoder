import os
from agents.utils import extract_code_blocks, textwrap
from evaluation.utils import call_llm
from utils.utils import file_to_string


class DirectAnswer:
    def __str__(self):
        return f"Directly Answer"

    def __init__(self, client, src_dir, timeout=10, model='openai/o3-mini', stage='encoder', previous_timestamp=None, final_iter=None, reasoning_effort='medium', **kwargs):
        self.client=client
        self.src_dir=src_dir
        self.timeout = timeout
        self.model = model
        self.stage = stage
        self.previous_timestamp = previous_timestamp
        self.final_iter = final_iter
        self.reasoning_effort = reasoning_effort
        self.solution = None
        self.iteration = 0
        

    def step(self):
        if self.previous_timestamp is not None and self.final_iter is not None:
            prompt = file_to_string(os.path.join(self.src_dir, "outputs", "prompts", self.previous_timestamp, f'prompt_iter_{self.final_iter}_{self.stage}.txt' ))
        else:
            prompt = file_to_string(os.path.join(self.src_dir, "prompts", "common", f"trivial_{self.stage}_prompt.txt"))
        self.solution = prompt
        return prompt

    def feedback(self, score, feedback, ):
        return

    def finalize(self):
        return self.solution
