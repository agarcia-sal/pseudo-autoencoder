from collections import defaultdict
from typing import List, Dict

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        graph: Dict[str, Dict[str, float]] = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def dfs(start: str, end: str, visited: set) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        visited.remove(start)
                        return weight * res
            visited.remove(start)
            return -1.0

        results = []
        for start, end in queries:
            result = dfs(start, end, set())
            results.append(result)

        return results