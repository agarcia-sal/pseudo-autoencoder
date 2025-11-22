from collections import defaultdict
from typing import List, Dict, Set

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph: Dict[str, Dict[str, float]] = defaultdict(dict)
        for (variable_a, variable_b), value in zip(equations, values):
            graph[variable_a][variable_b] = value
            graph[variable_b][variable_a] = 1.0 / value

        def dfs(start: str, end: str, visited: Set[str]) -> float:
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

        results: List[float] = []
        for query in queries:
            start, end = query
            visited: Set[str] = set()
            result = dfs(start, end, visited)
            results.append(result)

        return results