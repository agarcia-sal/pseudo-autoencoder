from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.initialize_graph()

        for (first_element, second_element), value in zip(equations, values):
            graph[first_element][second_element] = value
            graph[second_element][first_element] = 1 / value

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
            visited = set()
            result = dfs(start, end, visited)
            results.append(result)

        return results

    def initialize_graph(self):
        return defaultdict(dict)