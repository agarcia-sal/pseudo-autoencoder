from math import inf
from collections import defaultdict

class Solution:
    def minTrioDegree(self, n, edges):
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = inf
        trio_found = False

        for i in range(1, n - 1):
            neighbors_i = graph[i]
            for j in range(i + 1, n):
                if j not in neighbors_i:
                    continue
                neighbors_j = graph[j]
                for k in range(j + 1, n + 1):
                    if k in neighbors_i and k in neighbors_j:
                        trio_found = True
                        trio_degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        if trio_degree < min_degree:
                            min_degree = trio_degree

        return min_degree if trio_found else -1