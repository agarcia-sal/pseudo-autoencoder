# Pseudo-Autoencoder: Large Language Models for Examining Pseudocode Validity

# CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization


![example](https://github.com/user-attachments/assets/faf29c44-4904-4d74-9a15-37a038b14e77)

**Paper:** [CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization](https://arxiv.org/abs/2504.04310)

**Data:** [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset) and [HumanEval](https://github.com/openai/human-eval)

# Download Data
Download the raw data from [HumanEval](https://github.com/openai/human-eval) to the local directory `dataset/human_eval` and LeetCodeDataset-v0.3.0-train.jsonl and LeetCodeDataset-v0.3.0-test.jsonl from [LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset)

# Agent Implementations

Agents are implemented in the `agents` module. Currently supported agents include: `GreedyRefine`, `DirectAnswer`

Each agent implements the following functions:
- `step()`: Returns the next candidate prompt for evaluation.
- `feedback()`: Accepts evaluation results of previous candidate prompt and returns feedback for LLM prompt.
- `finalize()`: Returns the final prompt.

# Pipeline selection

There are 3 pipelines available to run: Autoencoder, Cosmetic, and Classifier

Set the `evolving_encoding`, `evolving_decoding`, `evolving_cosmetic`, `evolving_classifier` flag to True depending on which pipeline you want to run. For the autoencoder pipeline, set the `evolving_encoding` to True and `evolving_decoding` flag to False to start off with. The flags will toggle as the autoencoder switches between these two stages.

Depending on which pipeline you are running, set the correct `problems_dir_name` under which you will be operating. For the autoencoder, choose either `problems_dir_name = leet_code` or `problems_dir_name = human_eval`

Set the number of iterations you want to run. Default is 32

# Autoencoder Pipeline
![image](https://github.com/user-attachments/assets/b1206bfb-711e-4f4b-ab11-c096df4286cd)
Below is code to run the autoencoder with *Greedy Refinement* agent for LeetCode dataset for 32 iterations.
```python
from agents import GreedyRefine, DirectAnswer, FunSearch, AIDE, ChainOfExperts, ReEvo, BestOfN
from evaluation import Evaluator, get_data

# Load data
data = get_data('Aircraft landing', src_dir='data')

# Define agent, here we use GreedyRefine
agent = GreedyRefine(
    problem_description=data.problem_description,
    timeout=10,
    model='openai/o3-mini', # We use LiteLLM to call API
)

# Load evaluator
evaluator = Evaluator(data, timeout=10)

# Run for 64 iterations
for it in range(64):
    code = agent.step()
    if code is None:  # agent decides to terminate
        break
    feedback = evaluator.evaluate(code)  # Run evaluation
    agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback

# Get the final solution
code = agent.finalize()
feedback = evaluator.evaluate(code)
print(feedback.test_feedback)  # Test set score
```


**Evaluation on All Tasks**

```python
TASK_LIST = ['Aircraft landing', 'Assignment problem', 'Assortment problem', 'Bin packing - one-dimensional', 'Capacitated warehouse location', 'Common due date scheduling', 'Constrained guillotine cutting', 'Constrained non-guillotine cutting', 'Container loading', 'Container loading with weight restrictions', 'Corporate structuring', 'Crew scheduling', 'Equitable partitioning problem', 'Euclidean Steiner problem', 'Flow shop scheduling', 'Generalised assignment problem', 'Graph colouring', 'Hybrid Reentrant Shop Scheduling', 'Job shop scheduling', 'Maximal independent set', 'Multi-Demand Multidimensional Knapsack problem', 'Multidimensional knapsack problem', 'Open shop scheduling', 'Packing unequal circles', 'Packing unequal circles area', 'Packing unequal rectangles and squares', 'Packing unequal rectangles and squares area', 'Resource constrained shortest path', 'Set covering', 'Set partitioning', 'Travelling salesman problem', 'Uncapacitated warehouse location', 'Unconstrained guillotine cutting', 'Vehicle routing: period routing', 'p-median - capacitated', 'p-median - uncapacitated']

for task in TASK_LIST:
    ... # Run evaluation on one task
```

<details>
<summary><strong>Using Agents on Custom Problems</strong></summary>

Step 1: Include a concise description and a solve template. For example:

```python
problem_description = '''The Traveling Salesman Problem (TSP) is a classic combinatorial optimization problem where, given a set of cities with known pairwise distances, the objective is to find the shortest possible tour that visits each city exactly once and returns to the starting city. More formally, given a complete graph G = (V, E) with vertices V representing cities and edges E with weights representing distances, we seek to find a Hamiltonian cycle (a closed path visiting each vertex exactly once) of minimum total weight.

Implement in Solve Function

def solve(**kwargs):
    """
    Solve a TSP instance.

    Args:
        - nodes (list): List of (x, y) coordinates representing cities in the TSP problem
                      Format: [(x1, y1), (x2, y2), ..., (xn, yn)]

    Returns:
        dict: Solution information with:
            - 'tour' (list): List of node indices representing the solution path
                           Format: [0, 3, 1, ...] where numbers are indices into the nodes list
    """

    return {
        'tour': [],
    }
'''
```
Step 2: Define the agent
```python
from agents import GreedyRefine
agent = GreedyRefine(
    problem_description=problem_description,
    timeout=10,
    model='openai/o3-mini')
```
Step 3: Define the `evaluate` function and run the loop. Use the evaluate function to get results on the data, and iteratively improve the solution based on feedback:
```python
evaluate = ...  # Define evaluate() to return score (float) and feedback (str)
# Run for 64 iterations
for it in range(64):
    code = agent.step()
    dev_score, dev_feedback = evaluate(code) # Define evaluate() to return score (float) and feedback (str)
    agent.feedback(dev_score, dev_feedback) 

# Get the final soltuion
code = agent.finalize()
print(code)
```
</details>

*Docker environment for sandboxed agent execution and solution evaluation: coming soon.*

# Evaluation on FrontierCO

Download the raw data from [https://huggingface.co/datasets/CO-Bench/FrontierCO](https://huggingface.co/datasets/CO-Bench/FrontierCO) to the local directory `data`:

```
huggingface-cli download CO-Bench/FrontierCO --repo-type dataset --local-dir data
```
or

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id='CO-Bench/FrontierCO',
    repo_type='dataset',
    local_dir='data'
)
```

Note: In FrontierCO, instead of returning a single solution, the solve function must **yield increasingly better solutions** over time. The solve template looks like this:

```python
def solve(**kwargs):
    """
    Solve a TSP instance.

    Args:
        - nodes (list): List of (x, y) coordinates representing cities in the TSP problem.
                        Format: [(x1, y1), (x2, y2), ..., (xn, yn)]

    Yields:
        dict: Solution information with:
            - 'tour' (list): List of node indices representing the solution path.
                             Format: [0, 3, 1, ...] where numbers are indices into the nodes list.
    """
    # Your function must yield multiple solutions over time, not just return one.
    # Use Python's yield keyword repeatedly to produce a stream of solutions.
    # Each yielded solution should be better than the previous one.
    # Evaluation is based on the last yielded solution before timeout.
    while True:
        yield {
            'tour': [],
        }
```

Compared with CO-Bench, we use new agent implementations in FrontierCO:

```python
from agents import YieldGreedyRefine, YieldFunSearch, YieldReEvo

# And a new evaluator to fetch solutions yielded by the solver,
# evaluating only the last solution before timeout:
from evaluation import YieldingEvaluator, get_new_data

# Load data
data = get_new_data(task, src_dir='data', data_dir='data')

# Define agent (example: YieldGreedyRefine)
agent = YieldGreedyRefine(
    problem_description=data.problem_description,
    timeout=300,  # 300s timeout during solver development
    model='openai/o3-mini',  # We use LiteLLM to call the API
)

# Load YieldingEvaluator
# 300s timeout during solver development
evaluator = YieldingEvaluator(data, timeout=300)

# Run for 64 iterations
for it in range(64):
    code = agent.step()
    if code is None:  # agent decides to terminate
        break
    feedback = evaluator.evaluate(code)  # Run evaluation
    agent.feedback(feedback.dev_score, feedback.dev_feedback)  # Use dev set score as feedback

# Get the final solution
code = agent.finalize()

# For final evaluation, run the solver for 1 hour
final_evaluator = YieldingEvaluator(data, timeout=60 * 60)
feedback = final_evaluator.evaluate(code)
print(feedback.test_feedback)  # Test set score
```

