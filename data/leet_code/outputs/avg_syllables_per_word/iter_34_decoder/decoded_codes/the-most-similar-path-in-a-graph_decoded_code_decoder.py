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
            # Base case: first position in targetPath
            if i == 0:
                cost = 0 if names[j] == targetPath[i] else 1
                return cost, [j]

            min_cost = inf
            min_path = []
            for k in graph[j]:
                cost_k, path_k = dp(i - 1, k)
                if cost_k < min_cost:
                    min_cost = cost_k
                    min_path = path_k
            current_cost = min_cost + (0 if names[j] == targetPath[i] else 1)
            return current_cost, min_path + [j]

        min_cost = inf
        min_path = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path