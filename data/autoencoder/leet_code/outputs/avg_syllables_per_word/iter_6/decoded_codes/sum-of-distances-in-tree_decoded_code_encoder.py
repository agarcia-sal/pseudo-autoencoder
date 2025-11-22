from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n, edges):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n
        dist = [0] * n

        def dfs1(u, p):
            for v in graph[u]:
                if v != p:
                    dfs1(v, u)
                    count[u] += count[v]
                    dist[u] += dist[v] + count[v]

        dfs1(0, -1)

        def dfs2(u, p):
            for v in graph[u]:
                if v != p:
                    dist[v] = dist[u] - count[v] + (n - count[v])
                    dfs2(v, u)

        dfs2(0, -1)

        return dist