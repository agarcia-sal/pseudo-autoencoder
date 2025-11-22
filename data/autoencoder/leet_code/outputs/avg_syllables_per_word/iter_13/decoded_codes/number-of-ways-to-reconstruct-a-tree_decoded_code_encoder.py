from collections import defaultdict
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        # Find the node with the maximum degree
        max_degree = max(graph, key=lambda k: len(graph[k]))
        n = len(graph)

        # The root must connect to all other nodes
        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            # All neighbors of v must be neighbors of u or be u
            return all(neighbor in graph[u] or neighbor == u for neighbor in graph[v])

        ways = 1
        for u in graph:
            if u == max_degree:
                continue
            parent = None
            for v in graph[u]:
                if v in graph and len(graph[v]) >= len(graph[u]) and can_be_parent(v, u):
                    if parent is None or len(graph[v]) < len(graph[parent]):
                        parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == len(graph[u]):
                ways = 2
        return ways