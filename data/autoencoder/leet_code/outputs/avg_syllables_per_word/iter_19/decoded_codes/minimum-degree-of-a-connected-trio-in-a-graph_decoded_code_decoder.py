from math import inf
from collections import defaultdict

class Solution:
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = inf
        trio_found = False

        for i in range(1, n + 1):
            neighbors_i = graph[i]
            # Only check j in neighbors of i to reduce iterations
            for j in neighbors_i:
                if j <= i:
                    continue
                neighbors_j = graph[j]
                # Only check k in intersection of neighbors of i and neighbors of j to reduce iterations
                common_neighbors = neighbors_i & neighbors_j
                for k in common_neighbors:
                    if k <= j:
                        continue
                    # Found trio i, j, k
                    trio_found = True
                    degree_sum = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                    if degree_sum < min_degree:
                        min_degree = degree_sum

        return min_degree if trio_found else -1