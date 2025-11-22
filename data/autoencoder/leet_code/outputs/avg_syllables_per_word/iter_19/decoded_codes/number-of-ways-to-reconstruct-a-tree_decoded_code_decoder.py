from collections import defaultdict

class Solution:
    def checkWays(self, pairs):
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        if not graph:
            return 0

        max_degree = max(graph, key=lambda node: len(graph[node]))
        n = len(graph)

        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u, v):
            # Every neighbor of v must be in neighbors of u or equal to u
            return all(neigh == u or neigh in graph[u] for neigh in graph[v])

        ways = 1

        for u in graph:
            if u == max_degree:
                continue
            parent = None
            deg_u = len(graph[u])
            for v in graph[u]:
                if v in graph:
                    deg_v = len(graph[v])
                    if deg_v >= deg_u and can_be_parent(v, u):
                        if parent is None or deg_v < len(graph[parent]):
                            parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == deg_u:
                ways = 2

        return ways