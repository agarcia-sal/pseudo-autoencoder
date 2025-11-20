from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Union
import itertools

import numpy as np
import tqdm
# import fire

from .data import read_jsonl, write_jsonl, read_problems, get_problem_file, extract_completion, get_nested, code_extract
from .execution import check_correctness


def estimate_pass_at_k(
    num_samples: Union[int, List[int], np.ndarray],
    num_correct: Union[List[int], np.ndarray],
    k: int
) -> np.ndarray:
    """
    Estimates pass@k of each problem and returns them in an array.
    """

    def estimator(n: int, c: int, k: int) -> float:
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])


def evaluate_functional_correctness(
    # sample_file: str,
    dataset_name: str,
    problem_file: str,
    task_pseudocodes_codes: Dict, 
    # k: List[int],
    version: str = 'v0.3.0',
    split: str = 'test',
    n_workers: int = 4, # was 4
    timeout: float = 3.0,
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl"
    """

    # problem_file = get_problem_file(version, split)

    # problems = read_problems(problem_file)

    # Check the generated samples against test suites.
    # with ThreadPoolExecutor(max_workers=n_workers) as executor:

    futures = []
    completion_id = Counter()
    n_samples = 0
    results = defaultdict(list)
    errors = {}

    print("Reading samples...")
    for problem in tqdm.tqdm(read_jsonl(problem_file)):
        task_id = problem["task_id"]
        # completion = problem["completion"]
        decoded_code = task_pseudocodes_codes[task_id]["decoded_code"]
        args = (dataset_name, problem, decoded_code, timeout, completion_id[task_id]) # [TO DO]: change completion to decoded code i believe
        # print('args in evaluate_function_correctness:')
        # print(args)
        result = check_correctness(*args)
        # print('result within evaluate_functional_correctness:')
        # print(result)
        futures.append(result)

        if result and (not result["passed"]): 
            test_results = result["test_results"]
            test_errors = []
            for test in test_results:
                if not test["passed"]:
                    test_errors.append(test["error"])
            if test_errors:
                errors[task_id] = test_errors
        # else:
        #     errors.append(None)
        # future = executor.submit(check_correctness, *args)
        # futures.append(future)
        completion_id[task_id] += 1
        n_samples += 1

    # assert len(completion_id) == len(problems), "Some problems are not attempted."

    print("Running test suites...")
    for result in tqdm.tqdm(futures, total=len(futures)):
        results[result["task_id"]].append((result["completion_id"], result))

    # Reformat case results:
    problem_results = {}
    for result in results.values():
        # print('result in results.values() in evaluate_functional_correctness')
        # print(result)
        problem_id = result[0][1]["task_id"]
        test_results = result[0][1]["test_results"]
        # print('\ntest_result:')
        # print(test_results)
        case_result = [1 if r["passed"] else 0 for r in test_results]
        # print('case result:')
        # print(case_result)
        problem_results[problem_id] = (case_result, None) # format of CO-Bench paper
    return problem_results, errors
    
    ####### original: with ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=n_workers) as executor:

        futures = []
        completion_id = Counter()
        n_samples = 0
        results = defaultdict(list)

        print("Reading samples...")
        for problem in tqdm.tqdm(read_jsonl(problem_file)):
            task_id = problem["task_id"]
            # completion = problem["completion"]
            decoded_code = task_pseudocodes_codes[task_id]["decoded_code"]
            args = (problem, decoded_code, timeout, completion_id[task_id]) # [TO DO]: change completion to decoded code i believe
            future = executor.submit(check_correctness, *args)
            futures.append(future)
            completion_id[task_id] += 1
            n_samples += 1

        # assert len(completion_id) == len(problems), "Some problems are not attempted."

        print("Running test suites...")
        for future in tqdm.tqdm(as_completed(futures), total=len(futures)):
            result = future.result()
            results[result["task_id"]].append((result["completion_id"], result))

    # Reformat case results:
    problem_results = {}
    for result in results.values():
        # print('result in results.values() in evaluate_functional_correctness')
        # print(result)
        problem_id = result[0][1]["task_id"]
        test_results = result[0][1]["test_results"]
        # print('\ntest_result:')
        # print(test_results)
        case_result = [1 if r["passed"] else 0 for r in test_results]
        # print('case result:')
        # print(case_result)
        problem_results[problem_id] = (case_result, None) # format of CO-Bench paper
    return problem_results

############################

    # Calculate pass@k.
    total, correct = [], []
    for result in results.values():
        result.sort()
        passed = [r[1]["passed"] for r in result]
        total.append(len(passed))
        correct.append(sum(passed))
    total = np.array(total)
    correct = np.array(correct)

    ks = k
    pass_at_k = {f"pass@{k}": estimate_pass_at_k(total, correct, k).mean()
                 for k in ks if (total >= k).all()}

    # Finally, save the results in one file:
    def combine_results():
        for sample in read_jsonl(sample_file):
            task_id = sample["task_id"]
            result = results[task_id].pop(0)
            sample["result"] = result[1]["result"]
            sample["passed"] = result[1]["passed"]
            yield sample

    out_file = sample_file + "_results.jsonl"
    print(f"Writing results to {out_file}...")
    write_jsonl(out_file, tqdm.tqdm(combine_results(), total=n_samples))

    return pass_at_k


def evaluate(
        task_decoded_codes: Dict, 
        predict_column: str = 'response',
        version: str = 'v0.3.0',
        split: str = 'test',
        k: str = "1,10,20,100"):
    """
    Evaluate the functional correctness of the LeetCoTE problems.
    """
    # problem_file = get_problem_file(version, split)
    # k = list(map(int, k.split(",")))

    # # prepare sample file
    # result = []
    # for sample in read_jsonl(input_file):
    #     assert 'task_id' in sample, f'`task_id` should be specified in {input_file}'
    #     text = get_nested(sample, predict_column)
    #     sample['completion'] = code_extract(text)
    #     result.append(sample)
    # assert '.jsonl' in input_file, 'input_file must be a jsonl file'
    # sample_file = input_file.replace('.jsonl', '_sample.jsonl')
    # write_jsonl(sample_file, result)

    # results = evaluate_functional_correctness(sample_file, problem_file, k)
    # print(results)
    problem_file = get_problem_file(version, split)

    # prepare sample file
    # result = []
    # for sample in read_jsonl(input_file):
    #     assert 'task_id' in sample, f'`task_id` should be specified in {input_file}'
    #     text = get_nested(sample, predict_column)
    #     sample['completion'] = code_extract(text)
    #     result.append(sample)
    # assert '.jsonl' in input_file, 'input_file must be a jsonl file'
    # sample_file = input_file.replace('.jsonl', '_sample.jsonl')
    # write_jsonl(sample_file, result)
    for problem in task_decoded_codes:
        decoded_code = task_decoded_codes[problem]

    # results = evaluate_functional_correctness(sample_file, problem_file, k)
    # print(results)


# def cli():
#     fire.Fire(evaluate)
# 
# 
# if __name__ == '__main__':
#     cli()