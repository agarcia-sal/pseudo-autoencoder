import json
from agents.utils import extract_code_blocks, textwrap
from evaluation.utils import call_llm
from dataclasses import dataclass
from typing import Optional
from utils.utils import *

@dataclass
class Solution:
    prompt: str
    score: Optional[float] = None
    feedback: Optional[str] = None
    response: Optional[str] = None
    iter: Optional[float] = None


class GreedyRefine:
    def __str__(self):
        return f"Greedy Refinement"

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

    def load_previous(self, previous_best_path):
        if os.path.exists(previous_best_path):
            with open(previous_best_path, "r") as f:
                previous_best = json.load(f)
                prompt = previous_best["prompt"]
                response = previous_best["response"]
                score = previous_best["score"]
                iter = previous_best["iter"]
                feedback = previous_best
                self.solution.append(Solution(prompt=prompt, score=score, feedback=feedback, response=response, iter=iter))
        else:
            raise ValueError("previous_best_path does not exist")

    def step(self):
        # print('calling step()')
        # print('self.solution: ', self.solution)
        if len(self.solution) == 0:
            prompt = file_to_string(f'{self.src_dir}/prompts/greedy_refine/initial_{self.stage}.txt').format(
                timeout=self.timeout,
            )
        else:
            # if self.stage == 'decoder':
            #     previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
            # else:
            #     previous_best = sorted(self.solution, key=lambda x: x.score)[0]
            previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
            prompt = file_to_string(f'{self.src_dir}/prompts/greedy_refine/general_{self.stage}.txt').format(
                prompt=previous_best.prompt,
                feedback=previous_best.feedback,
                timeout=self.timeout,
            )
            # print('prompt after the first round in agent step()', prompt)
        # response = call_llm(prompt, model=self.model, reasoning_effort=self.reasoning_effort)
        # print('right before call_llm() in agent.step()')
        response = call_llm(prompt, self.client, self.model, reasoning_effort=self.reasoning_effort)
        # print('right after call_llm() in agent.step()')
        # code_blocks = extract_code_blocks(response) #[TO DO]: change
        # code = textwrap.dedent(code_blocks[0]) #[TO DO]: change
        prompt = response
        self.solution.append(Solution(prompt=prompt, response=response)) #[TO DO]: change
        print(f'len self.solution in step() for stage: {self.stage}:')
        print(len(self.solution))
        # print(f'self.solution in step for stage: {self.stage}: ')
        # print(self.solution)
        self.iteration += 1
        return prompt
    
    def step_direct_answer(self):
        prompt = file_to_string(f"{self.src_dir}/prompts/greedy_refine/trivial_classifier.txt")
        response = call_llm(prompt, self.client, self.model, reasoning_effort=self.reasoning_effort)
        prompt = response
        self.solution.append(Solution(prompt=prompt, response=response))
        self.iteration += 1
        return prompt


    def feedback(self, score, feedback, iter):
        # print('in feedback() of greedy_define agent')
        
        self.solution[-1].score = score
        self.solution[-1].feedback = feedback
        self.solution[-1].iter = iter
        # print('self.solution: ', self.solution)
        return

    def finalize(self):
        # print('len self.solution in finalize()')
        # print(len(self.solution))
        previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
        # if self.stage == 'decoder':
        #     previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
        # else:
        #     previous_best = sorted(self.solution, key=lambda x: x.score)[0]
        return previous_best.prompt

    def get_previous_best(self):
        previous_best = sorted(self.solution, key=lambda x: x.score)[-1]
        return previous_best.prompt, previous_best.score, previous_best.feedback, previous_best.iter