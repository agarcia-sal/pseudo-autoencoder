from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n  # number of nodes in subtree rooted at i
        dist = [0] * n   # sum of distances from node i to nodes in its subtree

        def dfs1(u: int, p: int) -> None:
            for v in graph[u]:
                if v != p:
                    dfs1(v, u)
                    count[u] += count[v]
                    dist[u] += dist[v] + count[v]

        dfs1(0, -1)

        def dfs2(u: int, p: int) -> None:
            for v in graph[u]:
                if v != p:
                    dist[v] = dist[u] - count[v] + (n - count[v])
                    dfs2(v, u)

        dfs2(0, -1)

        return dist