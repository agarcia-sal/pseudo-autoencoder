from typing import List, Set, Dict
import math

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency sets for each node (1-indexed)
        graph: Dict[int, Set[int]] = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = math.inf
        trio_found = False

        # For every triple (i, j, k), i < j < k, check if all edges exist between them
        # If yes, compute the trio degree and update min_degree
        for i in range(1, n - 1):
            neighbors_i = graph[i]
            for j in range(i + 1, n):
                # Quick check if edge i-j exists
                if j not in neighbors_i:
                    continue
                neighbors_j = graph[j]
                for k in range(j + 1, n + 1):
                    # Check both edges i-k and j-k
                    if k in neighbors_i and k in neighbors_j:
                        # Trio found
                        trio_found = True
                        # Trio degree is sum of degrees of i, j, k minus 6 (edges of the trio counted twice)
                        trio_degree = len(neighbors_i) + len(neighbors_j) + len(graph[k]) - 6
                        if trio_degree < min_degree:
                            min_degree = trio_degree

        return min_degree if trio_found else -1