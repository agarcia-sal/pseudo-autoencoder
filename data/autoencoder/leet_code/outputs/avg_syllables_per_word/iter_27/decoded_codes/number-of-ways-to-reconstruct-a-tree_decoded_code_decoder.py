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

        max_degree = max(graph, key=lambda k: len(graph[k]))
        n = len(graph)

        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            neighbors_v = graph[v]
            neighbors_u = graph[u]
            for neighbor in neighbors_v:
                if neighbor != u and neighbor not in neighbors_u:
                    return False
            return True

        ways = 1
        for u in graph:
            if u == max_degree:
                continue

            parent = None
            deg_u = len(graph[u])
            for v in graph[u]:
                # v must be in graph keys - ensured by graph construction
                deg_v = len(graph[v])
                if deg_v >= deg_u and can_be_parent(v, u):
                    if parent is None or deg_v < len(graph[parent]):
                        parent = v

            if parent is None:
                return 0

            if len(graph[parent]) == deg_u:
                ways = 2

        return ways