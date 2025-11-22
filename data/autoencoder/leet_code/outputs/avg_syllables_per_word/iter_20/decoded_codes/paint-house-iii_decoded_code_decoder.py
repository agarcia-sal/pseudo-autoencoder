from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')

        @lru_cache(maxsize=None)
        def dp(i: int, prev_color: int, groups: int) -> int:
            if i == m:
                return 0 if groups == target else INF

            if houses[i] != 0:
                new_groups = groups + (houses[i] != prev_color)
                return dp(i + 1, houses[i], new_groups)

            min_cost = INF
            for color in range(1, n + 1):
                new_groups = groups + (color != prev_color)
                candidate_cost = cost[i][color - 1] + dp(i + 1, color, new_groups)
                if candidate_cost < min_cost:
                    min_cost = candidate_cost

            return min_cost

        result = dp(0, 0, 0)
        return result if result != INF else -1