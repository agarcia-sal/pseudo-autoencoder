from collections import defaultdict
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        max_degree = max(graph, key=lambda k: len(graph[k]))
        n = len(graph)

        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            # v's neighbors must be a subset of u's neighbors, except u itself
            for neighbor in graph[v]:
                if neighbor != u and neighbor not in graph[u]:
                    return False
            return True

        ways = 1

        for u in graph:
            if u == max_degree:
                continue

            parent = None
            u_neighbors_size = len(graph[u])
            for v in graph[u]:
                if v in graph and len(graph[v]) >= u_neighbors_size and can_be_parent(v, u):
                    if parent is None or len(graph[v]) < len(graph[parent]):
                        parent = v

            if parent is None:
                return 0

            if len(graph[parent]) == u_neighbors_size:
                ways = 2

        return ways