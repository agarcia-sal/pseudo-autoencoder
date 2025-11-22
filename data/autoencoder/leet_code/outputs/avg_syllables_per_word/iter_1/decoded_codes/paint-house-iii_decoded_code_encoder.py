from math import inf
from functools import lru_cache

def min_cost(houses, cost, m, n, target):
    @lru_cache(None)
    def dp(i, prev, groups):
        if i == m:
            return 0 if groups == target else inf
        if houses[i] != 0:
            ng = groups + (houses[i] != prev)
            return dp(i + 1, houses[i], ng)
        res = inf
        for c in range(1, n + 1):
            ng = groups + (c != prev)
            res = min(res, cost[i][c - 1] + dp(i + 1, c, ng))
        return res

    result = dp(0, 0, 0)
    return result if result != inf else -1