from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value

        def dfs(start: str, end: str, visited: set) -> float:
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result

            visited.remove(start)

            return -1.0

        results = []
        for query in queries:
            start, end = query
            results.append(dfs(start, end, set()))

        return results