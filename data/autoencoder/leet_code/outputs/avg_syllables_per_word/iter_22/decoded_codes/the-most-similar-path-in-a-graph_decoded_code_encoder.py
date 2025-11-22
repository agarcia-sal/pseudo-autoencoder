from typing import List, Tuple
from collections import defaultdict
import math

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)
        memo = {}

        def dp(i: int, j: int) -> Tuple[int, List[int]]:
            if i == 0:
                cost = 0 if names[j] == targetPath[i] else 1
                return cost, [j]
            if (i, j) in memo:
                return memo[(i, j)]

            min_cost = math.inf
            min_path = []
            for k in graph[j]:
                cost, path = dp(i - 1, k)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            current_cost = min_cost + (0 if names[j] == targetPath[i] else 1)
            result_path = min_path + [j]
            memo[(i, j)] = (current_cost, result_path)
            return memo[(i, j)]

        min_cost = math.inf
        min_path = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path