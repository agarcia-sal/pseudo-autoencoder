from math import inf
from collections import defaultdict

class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(set)
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
                for k in range(j + 1, n + 1):
                    if k in neighbors_i and k in neighbors_j:
                        trio_found = True
                        degree = len(neighbors_i) + len(neighbors_j) + len(graph[k]) - 6
                        if degree < min_degree:
                            min_degree = degree
        return min_degree if trio_found else -1