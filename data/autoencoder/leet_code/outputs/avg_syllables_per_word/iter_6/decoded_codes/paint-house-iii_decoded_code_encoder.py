from functools import cache
from math import inf

class Solution:
    def minCost(self, houses, cost, m, n, target):
        @cache
        def dp(i, prev_color, groups):
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

        res = dp(0, 0, 0)
        return -1 if res == inf else res