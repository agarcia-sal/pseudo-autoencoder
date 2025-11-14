from evaluation.utils import FileLock, ParallelRun, design_optimal, eval_all, filter_dev, filter_test, normalize_metrics, average_metrics, check_if_no_metrics, get_problem_passing_rates, get_problem_readability_scores, record_problem_scores, evaluate_classifier_prompt, evaluate_classifier_prompt_test
import os
import random
# import asyncio
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
    def __init__(self, data, timeout=10, cpu_num=None, feedback_length=64, line_count=20, example_count=8, num_errors_shown=1, classifier_count=4):
        self.data = data
        self.timeout = timeout
        data_size = {problem: [1] * len(
            self.data.load_data(f"{self.data.src_dir}/{self.data.dataset_name}/{problem}")) for problem in self.data.problem_cases}
        cpu_num = os.cpu_count() or cpu_num
        self.case_workers, self.instance_workers = design_optimal(data_size, cpu_num)
        self.feedback_length = feedback_length
        self.line_count = line_count
        self.example_count = example_count
        self.num_errors_shown = num_errors_shown
        self.classifier_count = classifier_count

    def get_feedback(self, results, avg_score, stage, pseudocodes, codes, errors):
        # print('pseudocodes:')
        # print(pseudocodes)
        # print(f'len of pseudocodes {len(pseudocodes)}\n')
        # print('codes:')
        # print(codes)
        # print(f'len of codes {len(codes)}\n')
        # print('errors:')
        # print(errors)
        # print(f'len of errors {len(errors)}\n')
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
        errors_length = len(errors.keys())
        indices = list(range(errors_length))
        
        # print('lenght of pseudocode_list:', len(pseudocode_list))
        # print('length of code_list: ', len(code_list))
        # random_indices = random.sample(indices, min(self.example_count, errors_length))
        random_task_ids = random.sample(sorted(errors.keys()), min(self.example_count, errors_length))
        # print('random_indices: ')
        # print(random_indices)

        # [TO DO]: make sure the order is preserved throughout so that pseudocode, code, and errors match
        # error_tuples = [errors[index] for index in random_indices]
        pseudocode_list = []
        code_list = []
        error_strings = []
        error_task_ids = set()
        # for task_id in error_entries:
        for task_id in random_task_ids:
            # task_id = error["task_id"]
            error_list = errors[task_id]
            error_task_ids.add(task_id)
            pseudocode_list.append(pseudocodes[task_id])
            code_list.append(codes[task_id])
            error_strings.append(str(error_list[:self.num_errors_shown]))
        # print('right after setting up error_tuples')
        # pseudocode_list = [pseudocode_list[index] for index in random_indices]
        # code_list = [code_list[index] for index in random_indices]
        # errors_list = [errors[index] for index in random_indices]

        if errors_length < self.example_count:
            pseudocode_task_ids = set(pseudocodes.keys())
            remaining_ids = pseudocode_task_ids - error_task_ids
            random_ids = random.sample(sorted(remaining_ids), min(self.example_count - errors_length, len(remaining_ids)))
            for task_id in random_ids:
                pseudocode_list.append(pseudocodes[task_id])
                code_list.append(codes[task_id])
                error_strings.append(None)
        # print('right after filling out the rest for pseudocodes and codes')
        # print('error_strings:')
        # print(error_strings)
        # print('len of error_strings:', len(error_strings))
        # pseudocode_indices = list(range(len(pseudo)))
        # print("errors_list:")
        # print(errors_list)
        # errors_list = errors

        pseudocode_list = ['\n'.join(pseudocode.split('\n')[:self.line_count]) for pseudocode in pseudocode_list] # line_count can be modified
        code_list = ['\n'.join(code.split('\n')[:self.line_count]) for code in code_list]
        assert len(pseudocode_list) == len(code_list)


        if stage == 'encoder':
            prev_score.append(f"The following are {self.line_count} lines of original code of a random subset of the problems along with their pseudocodes.")
            for idx in range(len(pseudocode_list)):
                prev_score.append(f"\nOriginal Code for Problem {idx+1}:\n" + code_list[idx])
                prev_score.append(f"\nPseudocode for Problem {idx+1}:\n" + pseudocode_list[idx])
                if error_strings[idx]:
                    prev_score.append(f"\nError(s) from the decoded code for Problem {idx+1}:\n" + error_strings[idx])
                    
        elif stage == 'decoder':
            prev_score.append(f"The following are {self.line_count} lines of pseudocode of a random subset of the problems along with their decoded codes.")
            for idx in range(len(pseudocode_list)):
                prev_score.append(f"\nPseudocode for Problem {idx+1}:\n" + pseudocode_list[idx])
                prev_score.append(f"\nDecoded code for Problem {idx+1}:\n" + code_list[idx])
                if error_strings[idx]:
                    prev_score.append(f"\nError(s) from the decoded code for Problem {idx+1}:\n" + error_strings[idx])
            # for problem, problem_dict in problem_pseudocode_code:
            #     prev_score.append(f"\nPseudocode for Problem {problem}:\n" + problem_dict["pseudocode"])
            #     prev_score.append(f"\nDecoded code for Problem {problem}:\n" + problem_dict["code"])
        elif stage == 'cosmetic':
            prev_score.append(f"The following are {self.line_count} lines of original pseudocode of a random subset of the problems along with their modified pseudocodes.")
            for idx in range(len(pseudocode_list)):
                prev_score.append(f"\nPseudocode for Problem {idx+1}:\n" + pseudocode_list[idx])
                prev_score.append(f"\nModified Pseudocode for Problem {idx+1}:\n" + code_list[idx])
                # if error_strings[idx]:
                #     prev_score.append(f"\nError(s) from the decoded code for Problem {idx+1}:\n" + error_strings[idx])

        prev_score = '\n'.join(prev_score)

        if stage == 'encoder':
            # prev_score += f'\nAvg Passing Rate Minus Line Count: {avg_score}'
            # prev_score += f'\nScore of Average word length for ALL the problems: {avg_score}'
            prev_score += f'\nScore of (4*(Average syllables per word) + passing rate) for ALL the problems: {avg_score}'
            # prev_score += f'\nScore of (Average word length - average words per line) for ALL the problems: {avg_score}'
        elif stage == 'decoder':
            prev_score += f'\nAvg Passing Rate for ALL the problems: {avg_score}'
        elif stage == 'cosmetic':
            # prev_score += f'\nScore of Passing Rate - BLEU Score for ALL the problems: {avg_score}'
            prev_score += f'\nScore of -1*(BLEU Score) for ALL the problems: {avg_score}'

        # print("PREV_SCORE:")
        # print(prev_score)
        # print('\n\n')
        return prev_score

    # def get_feedback_cosmetic(self, results, final_score, stage, pseudocodes, codes, errors):
    
    def get_feedback_classifier(self, mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics):
    # def get_feedback_classifier(self, mislabeled_problems, true_negative_errors, near_miss_errors, final_score, metrics):
        
        positives = mislabeled_positives[:self.classifier_count]
        cosmetic = mislabeled_cosmetic[:self.classifier_count]
        negatives = mislabeled_negatives[:self.classifier_count]
        near_misses = mislabeled_near_misses[:self.classifier_count]

        # negative_error_task_ids = set(true_negative_errors.keys())
        # near_miss_error_task_ids = set(near_miss_errors.keys())

        feedback = ''

        feedback = 'We have a 2 way split for the pseudocodes: true positives, which are pseudocodes that correspond to code that passes all test cases.\n'
        feedback += 'We also have true negatives, which are pseudocodes that correspond to code that do not pass all test cases.\n'
        # feedback += 'We have cosmetic, which are pseudocodes that are variations of the positive pseudocodes and also pass all test cases.\n'
        # feedback += 'We have near-misses, which are pseudocodes that correspond to code that almost passes all test cases but do not. They pass at least 80% of test cases\n'
        # feedback += f'Here is the score for this prompt on positive-labeled pseudocodes: {avg_metrics["true_positive"]}\n'
        # feedback += f'Here is the score for this prompt on negative-labeled pseudocodes: {avg_metrics["true_negative"]}\n'
        # feedback += f'Here is the score for this prompt on cosmetic-labeled pseudocodes: {avg_metrics["cosmetic"]}\n'
        # feedback += f'Here is the score for this prompt on near_miss-labeled pseudocodes: {avg_metrics["near_miss"]}\n\n'
        
        num_problems_shown = 2
        num_problems = 0
        # for task_id, mislabeled_list in mislabeled_problems.items():
            # if num_problems == num_problems_shown:
            #     break
            # num_problems += 1
            # feedback += f"The following is a true positive pseudocode for problem {task_id} that was mislabeled as not reproducible:\n"
            # feedback += mislabeled_list[0]["pseudocode"]+"\n"
            # # feedback += f"The following is a cosmetic change to the true positive pseudocode for problem {task_id} that was mislabeled as not reproducible:\n"
            # # feedback += mislabeled_list[1]["pseudocode"]+"\n"
            # feedback += f"The following is a true negative pseudocode for problem {task_id} that was mislabeled as reproducible:\n"
            # feedback += mislabeled_list[1]["pseudocode"]+"\n"
            # if true_negative_errors[task_id]:
            #     error_string = true_negative_errors[task_id]
            #     feedback += "Here are the errors for this pseudocode:\n"
            #     # feedback += str(error_list[:self.num_errors_shown]) + "\n"
            #     feedback += error_string + "\n"
            # feedback += f"The following is a near miss pseudocode for problem {task_id} that was mislabeled as reproducible:\n"
            # feedback += mislabeled_list[1]["pseudocode"]+"\n"
            # if near_miss_errors[task_id]:
            #     error_string = near_miss_errors[task_id]
            #     feedback += "Here are the errors for this pseudocode:\n"
            #     # feedback += str(error_list[:self.num_errors_shown]) + "\n"
            #     feedback += error_string + "\n"

        if positives:
            feedback += "The following are pseudocodes that are reproducible but were labeled as not:\n"
            for entry in positives:
                feedback += entry["pseudocode"]+"\n"
        # if cosmetic:
        #     feedback += "\nThe following are modified pseudocodes of other reproducible versions of pseudocode that are reproducible but were labeled as not:\n"
        #     for entry in cosmetic:
        #         # feedback += "original version of the pseudocode for this problem that is reproducible:\n" 
        #         # feedback += entry["true_positive"] + "\n"
        #         # feedback += "modified version of the pseudocode for this problem that is also reproducible:\n"
        #         feedback += entry["pseudocode"]+"\n"
        if negatives:
            feedback += "\nThe following are pseudocodes that are not reproducible but were labeled as reproducible:\n"
            for entry in negatives:
                feedback += entry["pseudocode"]+"\n"
                task_id = entry["task_id"]
                if true_negative_errors[task_id]:
                    error_string = true_negative_errors[task_id]
                    feedback += "Here are the errors for this pseudocode:\n"
                    # feedback += str(error_list[:self.num_errors_shown]) + "\n"
                    feedback += error_string + "\n"
                feedback += "Here is a version of the pseudocode that IS reproducible:\n"
                feedback += entry["true_positive"] + "\n"
        # if near_misses:
        #     feedback += "\nThe following are near-miss pseudocodes - they are almost reproducible but were labeled as reproducible:\n"
        #     for entry in near_misses:
        #         feedback += entry["pseudocode"]+"\n"
        #         feedback += f"Passing rate for this pseudocode: {entry['score']}, but was given a label of 1\n"
        #         task_id = entry["task_id"]
        #         if near_miss_errors[task_id]:
        #             error_string = near_miss_errors[task_id]
        #             feedback += "Here are the errors for this pseudocode:\n"
        #             # feedback += str(error_list[:self.num_errors_shown]) + "\n"
        #             feedback += error_string + "\n"
        #         feedback += "Here is a version of the pseudocode that IS reproducible:\n"
        #         feedback += entry["true_positive"] + "\n"
        
        feedback += f'\nAvg Score for all pseudocodes: {final_score}'

        # print('feedback: ')
        # print(feedback)

        # Average metrics
        
        # print('after average metrics')
        

        # problem_accuracy_scores = get_problem_readability_scores(metrics, "accuracy_score")
        # print('after getting problem accuracy scores')
        # avg_metrics = record_problem_scores(problem_accuracy_scores, avg_metrics, "accuracy_score") # add the problem passing rates to the metrics

        # print('rigth before returning from getting feedback')
        return feedback

    # def evaluate_classifier(self, prompt, decoder_prompt, stage, timestamp, it, client):
    def evaluate_classifier(self, prompt, client, pseudocode_path, split='train'):
        # runtime = ParallelRun(evaluate_instance)
        # with FileLock():
        #     results, metrics, original_pseudocodes, pseudocodes, errors = runtime(
        #         self.data.problem_cases, self.data.dataset_name, self.data.problems_file_name, prompt, decoder_prompt,
        #         self.data.config_path, self.data.src_dir, stage, timestamp, it, client,
        #         timeout=self.timeout, instance_workers=self.instance_workers, case_workers=self.case_workers)

        # [TO DO]: set up self.data.train_set_filename
        problems_file_name = ''
        if split == 'train':
            problems_file_name = self.data.train_set_filename
        elif split == 'dev':
            problems_file_name = self.data.dev_set_filename
        elif split == 'test':
            problems_file_name = self.data.test_set_filename

        if split == 'train' or split 'dev':
            results = evaluate_classifier_prompt(problems_file_name, prompt, client)
            mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, labeled_correctly, true_negative_errors, near_miss_errors, final_score, metrics = results
            mislabeled = mislabeled_positives + mislabeled_cosmetic + mislabeled_negatives + mislabeled_near_misses
        elif split == 'test':
            results = evaluate_classifier_prompt_test(test_set_filename, prompt, client)
            mislabeled_positives, mislabeled_negatives, labeled_correctly, avg_metrics = results
            mislabeled = mislabeled_positives + mislabeled_negatives
        
        write_classifier_pseudocodes_to_file(labeled_correctly, os.path.join(pseudocode_path, "pass"))x
        write_classifier_pseudocodes_to_file(mislabeled, os.path.join(pseudocode_path, "fail"))

        feedback = self.get_feedback_classifier(mislabeled_positives, mislabeled_cosmetic, mislabeled_negatives, mislabeled_near_misses, true_negative_errors, near_miss_errors, final_score, metrics) 
        
        # problem_passing_rates = get_problem_passing_rates(results)
        # passing_rate = eval_all(results, self.data.problem_cases)

        metrics = check_if_no_metrics(metrics)
        avg_metrics = average_metrics(metrics) # averaged across all problems

        avg_metrics['final_score'] = final_score
        avg_metrics['avg_score'] = avg_metrics['accuracy_score']

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

    def evaluate_cosmetic(self, prompt, prev_stage_prompt, stage, timestamp, it, client):
        runtime = ParallelRun(evaluate_instance)
        with FileLock():
            results, metrics, original_pseudocodes, pseudocodes, errors = runtime(
                self.data.problem_cases, self.data.dataset_name, self.data.problems_file_name, prompt, prev_stage_prompt,
                self.data.config_path, self.data.src_dir, stage, timestamp, it, client,
                timeout=self.timeout, instance_workers=self.instance_workers, case_workers=self.case_workers)


        # print('results in evaluate_cosmetic:')
        # print(results)
        problem_passing_rates = get_problem_passing_rates(results)
        passing_rate = eval_all(results, self.data.problem_cases)

        metrics = check_if_no_metrics(metrics)
        # it's just the bleu score so no need to normalize
        avg_metrics = average_metrics(metrics) # averaged across all problems

        # final_score = passing_rate - avg_metrics['bleu_score'] 
        final_score = -1*avg_metrics['bleu_score']

        avg_metrics['passing_rate'] = passing_rate
        avg_metrics['avg_score'] = final_score

        problem_bleu_scores = get_problem_readability_scores(metrics, "bleu_score")
        avg_metrics = record_problem_scores(problem_passing_rates, avg_metrics, "passing_rate") # add the problem passing rates to the metrics
        avg_metrics = record_problem_scores(problem_bleu_scores, avg_metrics, "bleu_score") # add the problem avg word length to the metrics
        # avg_metrics = record_problem_scores(problem_conciseness_scores, avg_metrics, "avg_words_per_line") # add the problem avg word length to the metrics
        
        # feedback = self.get_feedback(results, dev_score)
        # print('right begore calling get_feedback')
        feedback = self.get_feedback(results, final_score, stage, pseudocodes, original_pseudocodes, errors)

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
        

    def evaluate(self, prompt, prev_stage_prompt, stage, timestamp, it, client):
        runtime = ParallelRun(evaluate_instance)
        with FileLock():
            results, metrics, pseudocodes, codes, errors = runtime(
                self.data.problem_cases, self.data.dataset_name, self.data.problems_file_name, prompt, prev_stage_prompt,
                self.data.config_path, self.data.src_dir, stage, timestamp, it, client,
                timeout=self.timeout, instance_workers=self.instance_workers, case_workers=self.case_workers)
        # print('results in evaluate(): ', results)
        # print('metrics in evaluate(): ', metrics)
        # results = self.data.norm_score(results) # [TO DO]: change this -> apply it to the metrics
        problem_passing_rates = get_problem_passing_rates(results)
        passing_rate = eval_all(results, self.data.problem_cases)
        # print('passing_rate in evaluate(): ', passing_rate)
        # dev_score = eval_all(filter_dev(results, self.data.get_dev()), self.data.problem_cases) # [TO DO]: uncomment and pass in a get_dev()
        # test_score = eval_all(filter_test(results, self.data.get_dev()), self.data.problem_cases) 
        metrics = check_if_no_metrics(metrics)
        normalized_metrics = normalize_metrics(metrics)
        # print('normalized_metrics in evaluate():', normalize_metrics)
        # problem_readability_scores = get_problem_readability_scores(metrics, "avg_word_length")
        # problem_readability_scores = get_problem_readability_scores(metrics, "readability")
        problem_readability_scores = get_problem_readability_scores(metrics, "avg_syllables_per_word")
        # problem_conciseness_scores = get_problem_readability_scores(metrics, "avg_words_per_line")
        avg_metrics = average_metrics(normalized_metrics)
        # avg_metrics = average_metrics(metrics)
        # print('avg_metrics in evaluate():', avg_metrics)
        if stage == 'encoder':
            # final_score = passing_rate + avg_metrics['avg_word_length'] # right now they have equal weight ?
            # final_score = avg_metrics['readability'] # right now they have equal weight ?
            # final_score = avg_metrics['line_length']
            # final_score = 0.5*passing_rate + 4*avg_metrics['avg_word_length'] - avg_metrics['avg_words_per_line']
            # final_score = avg_metrics['avg_word_length'] - avg_metrics['avg_words_per_line']
            # final_score = passing_rate + 4*avg_metrics['avg_word_length'] 
            final_score = passing_rate + 4*avg_metrics['avg_syllables_per_word'] 
            # final_score = avg_metrics['avg_word_length'] 
        else:
            final_score = passing_rate
            # final_score = avg_metrics['avg_syllables_per_word']
        # final_score = passing_rate
        avg_metrics['passing_rate'] = passing_rate
        avg_metrics['avg_score'] = final_score
        avg_metrics = record_problem_scores(problem_passing_rates, avg_metrics, "passing_rate") # add the problem passing rates to the metrics
        avg_metrics = record_problem_scores(problem_readability_scores, avg_metrics, "avg_syllables_per_word") # add the problem avg word length to the metrics
        # avg_metrics = record_problem_scores(problem_conciseness_scores, avg_metrics, "avg_words_per_line") # add the problem avg word length to the metrics

        # feedback = self.get_feedback(results, dev_score)
        feedback = self.get_feedback(results, final_score, stage, pseudocodes, codes, errors)
        # print('feedback in evaluate(): ')
        # print(feedback)
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