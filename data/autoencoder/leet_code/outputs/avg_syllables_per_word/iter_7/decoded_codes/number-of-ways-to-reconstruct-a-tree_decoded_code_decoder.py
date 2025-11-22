from collections import defaultdict
from typing import List, Set, Dict, Optional

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph: Dict[int, Set[int]] = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        max_degree = max(graph, key=lambda node: len(graph[node]))
        n = len(graph)
        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            for neighbor in graph[v]:
                if neighbor not in graph[u] and neighbor != u:
                    return False
            return True

        ways = 1

        for u in graph:
            if u == max_degree:
                continue
            parent: Optional[int] = None
            for v in graph[u]:
                if v in graph and len(graph[v]) >= len(graph[u]) and can_be_parent(v, u):
                    if parent is None or len(graph[v]) < len(graph[parent]):
                        parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == len(graph[u]):
                ways = 2

        return ways