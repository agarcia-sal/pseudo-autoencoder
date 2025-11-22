from collections import defaultdict
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        max_degree = max(graph, key=lambda x: len(graph[x]))
        n = len(graph)
        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            neighbors_v = graph[v]
            neighbors_u = graph[u]
            return all(neigh == u or neigh in neighbors_u for neigh in neighbors_v)

        ways = 1
        for u in graph:
            if u == max_degree:
                continue

            parent = None
            deg_u = len(graph[u])
            for v in graph[u]:
                if v in graph and len(graph[v]) >= deg_u and can_be_parent(v, u):
                    if parent is None or len(graph[v]) < len(graph[parent]):
                        parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == deg_u:
                ways = 2

        return ways