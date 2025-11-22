from collections import defaultdict
from functools import lru_cache
from typing import List, Tuple

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)

        @lru_cache(None)
        def dp(i: int, j: int) -> Tuple[int, List[int]]:
            if i == 0:
                cost = 0 if names[j] == targetPath[0] else 1
                return cost, [j]

            min_cost = float('inf')
            min_path: List[int] = []
            for k in graph[j]:
                cost, path = dp(i - 1, k)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            current_cost = min_cost + (0 if names[j] == targetPath[i] else 1)
            return current_cost, min_path + [j]

        min_cost = float('inf')
        min_path: List[int] = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path