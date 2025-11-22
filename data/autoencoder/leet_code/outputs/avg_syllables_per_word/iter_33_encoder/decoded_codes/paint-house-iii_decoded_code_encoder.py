from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(i: int, prev_color: int, groups: int) -> int:
            if i == m:
                return 0 if groups == target else inf

            if houses[i] != 0:
                new_groups = groups + (houses[i] != prev_color)
                return dp(i + 1, houses[i], new_groups)

            min_cost = inf
            for color in range(1, n + 1):
                new_groups = groups + (color != prev_color)
                current_cost = cost[i][color - 1] + dp(i + 1, color, new_groups)
                if current_cost < min_cost:
                    min_cost = current_cost

            return min_cost

        result = dp(0, 0, 0)
        return result if result != inf else -1