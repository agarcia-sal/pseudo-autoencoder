from math import inf
from typing import List, Set, Dict

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph: Dict[int, Set[int]] = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = inf
        trio_found = False

        for i in range(1, n + 1):
            neighbors_i = graph[i]
            for j in range(i + 1, n + 1):
                if j not in neighbors_i:
                    continue
                neighbors_j = graph[j]
                # Only check j if connected to i
                for k in range(j + 1, n + 1):
                    if k not in neighbors_i:
                        continue
                    if k not in neighbors_j:
                        continue
                    # trio found: i, j, k all mutually connected
                    trio_found = True
                    degree_sum = len(neighbors_i) + len(neighbors_j) + len(graph[k]) - 6
                    if degree_sum < min_degree:
                        min_degree = degree_sum

        return min_degree if trio_found else -1