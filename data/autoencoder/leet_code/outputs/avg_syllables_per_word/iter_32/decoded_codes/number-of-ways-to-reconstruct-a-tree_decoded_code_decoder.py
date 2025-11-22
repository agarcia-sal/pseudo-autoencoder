from collections import defaultdict
from typing import List, Set, Dict


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph: Dict[int, Set[int]] = defaultdict(set)
        # Build the undirected graph
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        if not graph:
            # No nodes => no valid tree
            return 0

        # Find the node with maximum degree
        max_degree_node = max(graph, key=lambda k: len(graph[k]))
        n = len(graph)

        # The root (max_degree_node) must be connected to all other nodes
        if len(graph[max_degree_node]) != n - 1:
            return 0

        def can_be_parent(u: int, v: int) -> bool:
            # v's neighbors must be subset of u's neighbors + possibly u itself
            # Since graph edges are undirected, and u is "parent" of v,
            # every neighbor of v except u must also be neighbor of u.
            for neighbor in graph[v]:
                if neighbor != u and neighbor not in graph[u]:
                    return False
            return True

        ways = 1

        for u in graph:
            if u == max_degree_node:
                continue

            parent = None
            deg_u = len(graph[u])

            # Candidate parents must have degree >= u and must satisfy can_be_parent
            for v in graph[u]:
                if v in graph:
                    deg_v = len(graph[v])
                    if deg_v >= deg_u and can_be_parent(v, u):
                        if parent is None or deg_v < len(graph[parent]):
                            parent = v

            if parent is None:
                return 0

            if len(graph[parent]) == len(graph[u]):
                ways = 2

        return ways