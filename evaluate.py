from evaluation.utils import FileLock, ParallelRun, design_optimal, eval_all, filter_dev, filter_test, normalize_metrics, average_metrics, check_if_no_metrics, get_problem_passing_rates, get_problem_readability_scores, record_problem_scores
import os
from dataclasses import dataclass


@dataclass
class Feedback:
    score: float
    dev_score: float
    test_score: float
    feedback: str
    dev_feedback: str
    test_feedback: str
    results: dict
    avg_metrics: dict


def evaluate_instance(instance, solve, eval_func):
    """Run solve and eval_func on the instance and return the score."""
    solution = solve(**instance)
    solution = {str(k): v for k, v in solution.items()}
    score = eval_func(**instance, **solution)
    return score


class Evaluator:
    def __init__(self, data, timeout=10, cpu_num=None, feedback_length=64, line_length=15):
        self.data = data
        self.timeout = timeout
        data_size = {problem: [1] * len(
            self.data.load_data(f"{self.data.src_dir}/{self.data.dataset_name}/{problem}")) for problem in self.data.problem_cases}
        cpu_num = os.cpu_count() or cpu_num
        self.case_workers, self.instance_workers = design_optimal(data_size, cpu_num)
        self.feedback_length = feedback_length
        self.line_length = line_length

    def get_feedback(self, results, avg_score, stage, pseudocode_list, code_list):
        prev_score = []
        # prev_score = []
        # for case in results.keys():
        #     scores, error_message = results.get(case, (None, "No result"))
        #     if error_message:
        #         prev_score.append(f"{case} -> Caught Error: {error_message}")
        #     else:
        #         # _scores = sorted(scores, key=lambda x: -1 if isinstance(x, str) else x)
        #         _scores = scores
        #         _scores = [x if isinstance(x, str) else f"{float(x):.3f}" for x in _scores][:self.feedback_length]
        #         prev_score.append(f"{case} -> Scores: {_scores}")
        # # prev_score = sorted(prev_score, key=lambda x: -1 if isinstance(x[0], str) else 1)
        # prev_score = '\n'.join(prev_score[:self.feedback_length])
        pseudocode_list = ['\n'.join(pseudocode.split('\n')[:self.line_length]) for pseudocode in pseudocode_list] # line_length can be modified
        code_list = ['\n'.join(code.split('\n')[:self.line_length]) for code in code_list]
        assert len(pseudocode_list) == len(code_list)

        if stage == 'encoder':
            prev_score.append(f"The follwing are {self.line_length} lines of original code of a random subset of the problems along with their pseudocodes.")
            for idx in range(len(pseudocode_list)):
                prev_score.append(f"\nOriginal Code for Problem {idx+1}:\n" + code_list[idx])
                prev_score.append(f"\nPseudocode for Problem {idx+1}:\n" + pseudocode_list[idx])
        elif stage == 'decoder':
            prev_score.append(f"The follwing are {self.line_length} lines of pseudocode of a random subset of the problems along with their decoded codes.")
            for idx in range(len(pseudocode_list)):
                prev_score.append(f"\nPseudocode for Problem {idx+1}:\n" + pseudocode_list[idx])
                prev_score.append(f"\nDecoded code for Problem {idx+1}:\n" + code_list[idx])

        prev_score = '\n'.join(prev_score)

        if stage == 'encoder':
            # prev_score += f'\nAvg Passing Rate Minus Line Count: {avg_score}'
            prev_score += f'\nFlesch Readability Ease for ALL the problems: {avg_score}'
        else:
            prev_score += f'\nAvg Passing Rate for ALL the problems: {avg_score}'
        return prev_score
    
    def get_feedback_classifier(self, final_score):
        feedback = f'\nAvg Score: {final_score}'

        return Feedback( # [TO DO]: change this back to the above Feedback
            score=final_score,
            dev_score=final_score,
            test_score=final_score,
            feedback=feedback,
            dev_feedback=feedback,
            test_feedback=feedback,
            results={}, 
            avg_metrics={},
        )

    def evaluate(self, prompt, prev_stage_prompt, stage, timestamp, it, client):
        runtime = ParallelRun(evaluate_instance)
        with FileLock():
            results, metrics, pseudocodes, codes = runtime(
                self.data.problem_cases, self.data.dataset_name, prompt, prev_stage_prompt,
                self.data.config_path, self.data.src_dir, stage, timestamp, it, client,
                timeout=self.timeout, instance_workers=self.instance_workers, case_workers=self.case_workers)
        print('results in evaluate(): ', results)
        # print('metrics in evaluate(): ', metrics)
        # results = self.data.norm_score(results) # [TO DO]: change this -> apply it to the metrics
        problem_passing_rates = get_problem_passing_rates(results)
        passing_rate = eval_all(results, self.data.problem_cases)
        print('passing_rate in evaluate(): ', passing_rate)
        # dev_score = eval_all(filter_dev(results, self.data.get_dev()), self.data.problem_cases) # [TO DO]: uncomment and pass in a get_dev()
        # test_score = eval_all(filter_test(results, self.data.get_dev()), self.data.problem_cases) 
        metrics = check_if_no_metrics(metrics)
        # normalized_metrics = normalize_metrics(metrics)
        # print('normalized_metrics in evaluate():', normalize_metrics)
        # problem_readability_scores = get_problem_readability_scores(metrics, "avg_word_length")
        problem_readability_scores = get_problem_readability_scores(metrics, "readability")
        avg_metrics = average_metrics(metrics)
        # print('avg_metrics in evaluate():', avg_metrics)
        if stage == 'encoder':
            # final_score = passing_rate + avg_metrics['avg_word_length'] # right now they have equal weight ?
            final_score = avg_metrics['readability'] # right now they have equal weight ?
            # final_score = avg_metrics['line_length']
            # final_score = avg_metrics['avg_syllables_per_word']
        else:
            final_score = passing_rate
            # final_score = avg_metrics['avg_syllables_per_word']
        # final_score = passing_rate
        avg_metrics['passing_rate'] = passing_rate
        avg_metrics['avg_score'] = final_score
        avg_metrics = record_problem_scores(problem_passing_rates, avg_metrics, "passing_rate") # add the problem passing rates to the metrics
        avg_metrics = record_problem_scores(problem_readability_scores, avg_metrics, "readability") # add the problem avg word length to the metrics

        # feedback = self.get_feedback(results, dev_score)
        feedback = self.get_feedback(results, final_score, stage, pseudocodes, codes)
        # print('feedback in evaluate():', feedback)
        # dev_feedback = self.get_feedback(filter_dev(results, self.data.get_dev()), dev_score)
        # test_feedback = self.get_feedback(filter_test(results, self.data.get_dev()), test_score)
        # return Feedback(
        #     score=score,
        #     dev_score=dev_score,
        #     test_score=test_score,
        #     feedback=feedback,
        #     dev_feedback=dev_feedback,
        #     test_feedback=test_feedback,
        #     results=results, 
        # )
        return Feedback( # [TO DO]: change this back to the above Feedback
            score=final_score,
            dev_score=final_score,
            test_score=final_score,
            feedback=feedback,
            dev_feedback=feedback,
            test_feedback=feedback,
            results=results, 
            avg_metrics=avg_metrics,
        )