from collections import defaultdict
from functools import lru_cache
from math import inf

class Solution:
    def mostSimilar(self, n, roads, names, targetPath):
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)

        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                if names[j] != targetPath[i]:
                    return 1, [j]
                else:
                    return 0, [j]

            min_cost = inf
            min_path = []
            for k in graph[j]:
                cost, path = dp(i - 1, k)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            current_cost = min_cost + (1 if names[j] != targetPath[i] else 0)
            return current_cost, min_path + [j]

        min_cost = inf
        min_path = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path