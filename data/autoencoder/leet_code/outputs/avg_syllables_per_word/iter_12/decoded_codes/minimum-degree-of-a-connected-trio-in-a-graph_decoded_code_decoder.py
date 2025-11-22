from math import inf
from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = inf
        trio_found = False

        # Iterate through all combinations of nodes (i, j, k) with i < j < k
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if j not in graph[i]:
                    continue  # Skip if no edge between i and j
                for k in range(j + 1, n + 1):
                    if k in graph[i] and k in graph[j]:
                        trio_found = True
                        trio_degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        if trio_degree < min_degree:
                            min_degree = trio_degree

        return min_degree if trio_found else -1