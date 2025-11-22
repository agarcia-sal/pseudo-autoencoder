from collections import defaultdict
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)
        # find node with max neighbors (degree)
        max_degree_node = max(graph, key=lambda k: len(graph[k]))
        n = len(graph)
        # Check if max_degree_node connects to all other nodes
        if len(graph[max_degree_node]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            neighbors_v = graph[v]
            neighbors_u = graph[u]
            # all neighbors of v must be neighbors of u or u itself
            for nei in neighbors_v:
                if nei != u and nei not in neighbors_u:
                    return False
            return True

        ways = 1
        for u in graph:
            if u == max_degree_node:
                continue
            parent = None
            size_u = len(graph[u])
            for v in graph[u]:
                if v in graph and len(graph[v]) >= size_u and can_be_parent(v, u):
                    if parent is None or len(graph[v]) < len(graph[parent]):
                        parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == size_u:
                ways = 2

        return ways