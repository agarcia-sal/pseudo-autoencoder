class Solution:
    def minCost(self, houses, cost, m, n, target):
        from functools import lru_cache
        INF = float('inf')

        @lru_cache(None)
        def dp(i, prev_color, groups):
            if i == m:
                return 0 if groups == target else INF

            if houses[i] != 0:
                new_groups = groups + (1 if houses[i] != prev_color else 0)
                return dp(i + 1, houses[i], new_groups)

            min_cost = INF
            for color in range(1, n + 1):
                new_groups = groups + (1 if color != prev_color else 0)
                current_cost = cost[i][color - 1] + dp(i + 1, color, new_groups)
                min_cost = min(min_cost, current_cost)

            return min_cost

        result = dp(0, 0, 0)
        return -1 if result == INF else result