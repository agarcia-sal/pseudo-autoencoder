from typing import List, Tuple, Dict
import sys
sys.setrecursionlimit(10**7)
from functools import lru_cache

class Solution:
    def mostSimilar(self, n: int, targetPath: List[str], roads: List[List[int]], names: List[str]) -> List[int]:
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)

        @lru_cache(None)
        def dp(i: int, j: int) -> Tuple[int, List[int]]:
            # Base case: first position in targetPath
            diff = 1 if names[j] != targetPath[i] else 0
            if i == 0:
                return diff, [j]

            min_cost = float('inf')
            min_path: List[int] = []
            for k in graph[j]:
                cost, path = dp(i - 1, k)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            # Add cost if current name differs from targetPath at position i
            current_cost = min_cost + diff
            return current_cost, min_path + [j]

        min_cost = float('inf')
        min_path: List[int] = []
        for j in range(n):
            cost, path = dp(m - 1, j)
            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path