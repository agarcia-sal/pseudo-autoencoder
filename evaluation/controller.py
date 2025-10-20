import os
from evaluation.utils import import_func, extract_function_source, list_problem_cases, list_jsonl_task_ids
from dataclasses import dataclass

from typing import Optional


@dataclass
class Data:
    config_path: str
    problem: str
    solve_template: str
    problem_description: str
    problem_cases: str
    norm_score: str
    get_dev: str
    dataset_name: str
    problems_file_name : str
    load_data: callable
    src_dir: str



TASK_LIST = ['Aircraft landing',
             'Assignment problem',
             'Assortment problem', 'Bin packing - one-dimensional',
             'Capacitated warehouse location', 'Common due date scheduling', 'Constrained guillotine cutting',
             'Constrained non-guillotine cutting', 'Container loading', 'Container loading with weight restrictions',
             'Corporate structuring', 'Crew scheduling', 'Equitable partitioning problem',
             'Euclidean Steiner problem', 'Flow shop scheduling', 'Generalised assignment problem', 'Graph colouring',
             'Hybrid Reentrant Shop Scheduling', 'Job shop scheduling', 'MIS',
             'Multi-Demand Multidimensional Knapsack problem', 'Multidimensional knapsack problem',
             'Open shop scheduling', 'Packing unequal circles', 'Packing unequal circles area',
             'Packing unequal rectangles and squares', 'Packing unequal rectangles and squares area',
             'Resource constrained shortest path', 'Set covering', 'Set partitioning', 'TSP',
             'Uncapacitated warehouse location', 'Unconstrained guillotine cutting',
             'Vehicle routing: period routing', 'p-median - capacitated', 'p-median - uncapacitated']


# def get_data(dataset_name, src_dir='data'):
#     load_data, _, problem = import_func(f"{src_dir}/{dataset_name}/config.py", 'load_data', 'eval_func', 'DESCRIPTION')
#     config_path = f"{src_dir}/{dataset_name}/config.py"
#     solve_template = extract_function_source(f"{src_dir}/{dataset_name}/config.py", 'solve')
#     problem_cases = list_problem_cases(f"{src_dir}/{dataset_name}")
#     try:
#         norm_score, = import_func(f"{src_dir}/{dataset_name}/config.py", 'norm_score')
#     except AttributeError:
#         norm_score = lambda x: x

#     try:
#         get_dev, = import_func(f"{src_dir}/{dataset_name}/config.py", 'get_dev')
#     except AttributeError:
#         get_dev = lambda: None
#     problem_description = f"{problem}\n\n## Implement in Solve Function\n\n{solve_template}"

#     return Data(
#         config_path=config_path,
#         dataset_name=dataset_name,
#         src_dir=src_dir,
#         load_data=load_data,
#         problem=problem,
#         solve_template=solve_template,
#         problem_description=problem_description,
#         problem_cases=problem_cases,
#         norm_score=norm_score,
#         get_dev=get_dev,
#     )
def get_data(dataset_name, problems_file_name, src_dir='data', version = 'v0.1.0', split='train'):
    # load_data, _, problem = import_func(f"{src_dir}/{dataset_name}/config.py", 'load_data', 'eval_func', 'DESCRIPTION')
    load_data = lambda x : x
    norm_score = lambda x : x
    # config_path = f"{src_dir}/{dataset_name}/config.py"
    # solve_template = extract_function_source(f"{src_dir}/{dataset_name}/config.py", 'solve')
    # problem_cases = list_problem_cases(f"{src_dir}/{dataset_name}")
    file_path = os.path.join(src_dir, dataset_name, problems_file_name)
    # if version != '':
    #     file_path += f"-{version}"
    # if split != '':
    #     file_path += f"-{split}"
    # file_path += '.jsonl'
    problem_cases = list_jsonl_task_ids(file_path)
    # try:
    #     norm_score, = import_func(f"{src_dir}/{dataset_name}/config.py", 'norm_score')
    # except AttributeError:
    #     norm_score = lambda x: x

    # try:
    #     get_dev, = import_func(f"{src_dir}/{dataset_name}/config.py", 'get_dev')
    # except AttributeError:
    #     get_dev = lambda: None
    # problem_description = f"{problem}\n\n## Implement in Solve Function\n\n{solve_template}"

    return Data(
        config_path='',
        dataset_name=dataset_name,
        problems_file_name=problems_file_name,
        src_dir=src_dir,
        load_data=load_data,
        problem='',
        solve_template='',
        problem_description='',
        problem_cases=problem_cases,
        norm_score=norm_score,
        get_dev='',
    )