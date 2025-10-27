from collections import defaultdict

class Solution:
    def checkWays(self, pairs):
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        n = len(graph)
        max_degree = max(graph, key=lambda x: len(graph[x]))
        if len(graph[max_degree]) != n - 1:
            return 0

        def can_be_parent(u, v):
            neighbors_v = graph[v]
            neighbors_u = graph[u]
            # All neighbors of v must be in neighbors of u (or be u itself)
            for neighbor in neighbors_v:
                if neighbor != u and neighbor not in neighbors_u:
                    return False
            return True

        ways = 1
        for u in graph:
            if u == max_degree:
                continue
            parent = None
            neighbors_u = graph[u]
            size_u = len(neighbors_u)
            for v in neighbors_u:
                if v in graph:
                    size_v = len(graph[v])
                    if size_v >= size_u and can_be_parent(v, u):
                        if parent is None or size_v < len(graph[parent]):
                            parent = v
            if parent is None:
                return 0
            if len(graph[parent]) == size_u:
                ways = 2

        return ways