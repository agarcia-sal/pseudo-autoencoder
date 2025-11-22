from math import inf
from functools import lru_cache

class Solution:
    def minCost(self, houses, cost, m, n, target):
        @lru_cache(None)
        def dp(i, prev_color, groups):
            if groups > target:
                return inf
            if i == m:
                return 0 if groups == target else inf
            if houses[i] != 0:
                new_groups = groups + (houses[i] != prev_color)
                return dp(i + 1, houses[i], new_groups)
            min_cost = inf
            for color in range(1, n + 1):
                new_groups = groups + (color != prev_color)
                curr_cost = cost[i][color - 1] + dp(i + 1, color, new_groups)
                if curr_cost < min_cost:
                    min_cost = curr_cost
            return min_cost

        result = dp(0, 0, 0)
        return result if result != inf else -1