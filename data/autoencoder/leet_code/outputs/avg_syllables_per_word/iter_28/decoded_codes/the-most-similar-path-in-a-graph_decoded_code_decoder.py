from collections import defaultdict
from typing import List, Tuple

class Solution:
    def mostSimilar(self, n: int, names: List[str], roads: List[List[int]], targetPath: List[str]) -> List[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)
        INF = float('inf')
        memo = {}

        def dp(i: int, j: int) -> Tuple[int, List[int]]:
            if (i, j) in memo:
                return memo[(i, j)]
            mismatch = 1 if names[j] != targetPath[i] else 0
            if i == 0:
                memo[(i, j)] = (mismatch, [j])
                return memo[(i, j)]

            min_cost = INF
            min_path = []
            for k in graph[j]:
                cost, path = dp(i - 1, k)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            total_cost = min_cost + mismatch
            memo[(i, j)] = (total_cost, min_path + [j])
            return memo[(i, j)]

        min_cost = INF
        min_path = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < min_cost:
                min_cost = cost
                min_path = path
        return min_path