from collections import defaultdict
from math import inf
from functools import lru_cache

class Solution:
    def mostSimilar(self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]) -> list[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)

        @lru_cache(None)
        def dp(i: int, j: int) -> tuple[int, list[int]]:
            if i == 0:
                cost_at_base = 0 if names[j] == targetPath[i] else 1
                return cost_at_base, [j]

            min_cost = inf
            min_path = []
            for k in graph[j]:
                cost, path = dp(i - 1, k)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            current_cost = min_cost if names[j] == targetPath[i] else min_cost + 1
            return current_cost, min_path + [j]

        overall_min_cost = inf
        overall_min_path = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < overall_min_cost:
                overall_min_cost = cost
                overall_min_path = path

        return overall_min_path