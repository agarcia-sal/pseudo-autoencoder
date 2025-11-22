from math import inf
from typing import List, Dict, Set

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = self.build_graph(n, edges)
        min_degree = inf
        trio_found = False
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if j not in graph[i]:
                    continue
                for k in range(j + 1, n + 1):
                    if k in graph[i] and k in graph[j]:
                        trio_found = True
                        trio_degree = self.calculate_trio_degree(graph, i, j, k)
                        if trio_degree < min_degree:
                            min_degree = trio_degree
        return min_degree if trio_found else -1

    def build_graph(self, n: int, edges: List[List[int]]) -> Dict[int, Set[int]]:
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return graph

    def calculate_trio_degree(self, graph: Dict[int, Set[int]], i: int, j: int, k: int) -> int:
        degree_i = len(graph[i])
        degree_j = len(graph[j])
        degree_k = len(graph[k])
        # Subtract 6 because the edges inside the trio (3 edges counted twice in degrees)
        total_degree = degree_i + degree_j + degree_k - 6
        return total_degree