from collections import defaultdict
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        if not graph:
            return 0

        max_degree = max(graph.keys(), key=lambda k: len(graph[k]))
        n = len(graph)

        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            # All neighbors of v must be in neighbors of u or u itself
            u_neighbors = graph[u]
            for neighbor in graph[v]:
                if neighbor != u and neighbor not in u_neighbors:
                    return False
            return True

        ways = 1

        for u in graph:
            if u == max_degree:
                continue

            parent = None
            u_deg = len(graph[u])

            for v in graph[u]:
                if v in graph:
                    v_deg = len(graph[v])
                    if v_deg >= u_deg and can_be_parent(v, u):
                        if parent is None or v_deg < len(graph[parent]):
                            parent = v

            if parent is None:
                return 0

            if len(graph[parent]) == u_deg:
                ways = 2

        return ways