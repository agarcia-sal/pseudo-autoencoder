from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (variable_a, variable_b), value in zip(equations, values):
            graph[variable_a][variable_b] = value
            graph[variable_b][variable_a] = 1 / value

        def dfs(start: str, end: str, visited: set) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    recursive_result = dfs(neighbor, end, visited)
                    if recursive_result != -1.0:
                        return weight * recursive_result
            visited.remove(start)
            return -1.0

        results = []
        for start, end in queries:
            visited = set()
            result = dfs(start, end, visited)
            results.append(result)

        return results