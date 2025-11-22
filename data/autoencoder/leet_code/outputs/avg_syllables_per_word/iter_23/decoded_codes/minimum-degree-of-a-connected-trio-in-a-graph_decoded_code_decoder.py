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
                # Candidates for k must be neighbors of both i and j
                common_neighbors = neighbors_i.intersection(neighbors_j)
                for k in common_neighbors:
                    if k <= j:
                        continue  # maintain order i < j < k to avoid duplicates
                    neighbors_k = graph[k]
                    # If k neighbors both i and j, trio found
                    trio_found = True
                    trio_degree = len(neighbors_i) + len(neighbors_j) + len(neighbors_k) - 6
                    if trio_degree < min_degree:
                        min_degree = trio_degree

        return min_degree if trio_found else -1