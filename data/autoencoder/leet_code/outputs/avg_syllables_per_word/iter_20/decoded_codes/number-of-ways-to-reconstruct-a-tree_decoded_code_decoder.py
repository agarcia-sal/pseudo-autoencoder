from collections import defaultdict

class Solution:
    def checkWays(self, pairs):
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

        def can_be_parent(u, v):
            # Check if neighbors of v are subset of neighbors of u or equal to u itself
            for nei in graph[v]:
                if nei != u and nei not in graph[u]:
                    return False
            return True

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