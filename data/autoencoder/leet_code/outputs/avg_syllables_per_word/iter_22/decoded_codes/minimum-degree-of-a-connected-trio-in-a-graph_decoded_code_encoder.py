from math import inf
from typing import List, Set, Dict

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph: Dict[int, Set[int]] = {i: set() for i in range(1, n+1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = inf
        trio_found = False

        # Iterate over all unique trios i < j < k
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                # Check if edge i-j exists before checking k to reduce work
                if j not in graph[i]:
                    continue
                for k in range(j+1, n+1):
                    if k in graph[i] and k in graph[j]:  # trio i,j,k is connected each pair
                        trio_found = True
                        # sum of degrees of i, j, k minus 6 to exclude edges inside trio counted twice
                        trio_degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        if trio_degree < min_degree:
                            min_degree = trio_degree

        return min_degree if trio_found else -1