from functools import cache
from math import inf

class Solution:
    def minCost(self, houses, cost, m, n, target):
        @cache
        def dp(i, prev_color, groups):
            if i == m:
                if groups == target:
                    return 0
                else:
                    return inf

            if houses[i] != 0:
                new_groups = groups + (1 if houses[i] != prev_color else 0)
                return dp(i + 1, houses[i], new_groups)

            min_cost = inf
            for color in range(1, n + 1):
                new_groups = groups + (1 if color != prev_color else 0)
                current_cost = cost[i][color - 1] + dp(i + 1, color, new_groups)
                if current_cost < min_cost:
                    min_cost = current_cost

            return min_cost

        result = dp(0, 0, 0)
        return result if result != inf else -1