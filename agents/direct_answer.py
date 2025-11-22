import os
from agents.utils import extract_code_blocks, textwrap
from evaluation.utils import call_llm
from utils.utils import file_to_string
from dataclasses import dataclass
from typing import Optional

@dataclass
class Solution:
    prompt: str
    score: Optional[float] = None
    feedback: Optional[str] = None
    iter: Optional[float] = None

class DirectAnswer:
    def __str__(self):
        return f"Directly Answer"

    def __init__(self, client, src_dir, timeout=10, model='openai/o3-mini', stage='encoder', reasoning_effort='medium', **kwargs):
        self.client=client
        self.src_dir=src_dir
        self.timeout = timeout
        self.model = model
        self.stage = stage
        self.reasoning_effort = reasoning_effort
        self.solution = []
        self.iteration = 0

    def set_prompt(self, cfg):
        
        if self.stage == 'encoder':
            self.prev_iter = cfg.prev_iter_encoder
            self.previous_timestamp = cfg.previous_autoencoder_label
        elif self.stage == 'decoder':
            self.prev_iter = cfg.prev_iter_decoder
            self.previous_timestamp = cfg.previous_autoencoder_label
        elif self.stage == 'cosmetic':
            self.prev_iter = cfg.prev_iter_cosmetic
            self.previous_timestamp = cfg.previous_cosmetic_label
        elif self.stage == 'classifier':
            self.previous_timestamp = cfg.previous_classifier_label
            self.prev_iter = cfg.prev_iter_classifier
        

    def step(self):
        if self.previous_timestamp is not None and self.prev_iter is not None:
            prompt = file_to_string(os.path.join(self.src_dir, "outputs", "prompts", self.previous_timestamp, f'prompt_iter_{self.prev_iter}_{self.stage}.txt' ))
        else:
            prompt = file_to_string(os.path.join(self.src_dir, "prompts", "common", f"trivial_{self.stage}_prompt.txt"))
        self.solution.append(Solution(prompt=prompt))
        return prompt

    def feedback(self, score, feedback, iter):
        self.solution[-1].score = score
        self.solution[-1].feedback = feedback
        self.solution[-1].iter = iter
        return

    def finalize(self):
        previous_best = self.solution[-1]
        # if self.stage == 'decoder':
        #     previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
        # else:
        #     previous_best = sorted(self.solution, key=lambda x: x.score)[0]
        return previous_best.prompt

    def get_previous_best(self):
        previous_best = self.solution[-1]
        return previous_best.prompt, previous_best.score, previous_best.feedback, previous_best.iter
