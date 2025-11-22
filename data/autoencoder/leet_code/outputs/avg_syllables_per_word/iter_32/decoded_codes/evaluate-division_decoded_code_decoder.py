from collections import defaultdict
from typing import List, Dict, Set

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        graph: Dict[str, Dict[str, float]] = defaultdict(dict)

        # Build graph: Both directions a->b = value and b->a = 1/value
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value

        def dfs(start: str, end: str, visited: Set[str]) -> float:
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
        for query in queries:
            start, end = query
            visited = set()
            results.append(dfs(start, end, visited))

        return results