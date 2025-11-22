from collections import defaultdict
from typing import List, Set, Dict, Optional

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # Build graph: node -> set of connected nodes
        graph: Dict[int, Set[int]] = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        # Find the node with maximum degree
        max_degree = max(graph, key=lambda k: len(graph[k]))
        n = len(graph)

        # Check if max_degree node is connected to all other nodes
        if len(graph[max_degree]) != n - 1:
            return 0

        # Helper function to check if 'u' can be parent of 'v'
        def can_be_parent(u: int, v: int) -> bool:
            neighbors_v = graph[v]
            neighbors_u = graph[u]
            for nb in neighbors_v:
                if nb != u and nb not in neighbors_u:
                    return False
            return True

        ways = 1
        for u in graph:
            if u == max_degree:
                continue
            parent: Optional[int] = None
            deg_u = len(graph[u])
            for v in graph[u]:
                if v in graph:
                    deg_v = len(graph[v])
                    if deg_v >= deg_u and can_be_parent(v, u):
                        if parent is None or len(graph[v]) < len(graph[parent]):
                            parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == deg_u:
                ways = 2

        return ways