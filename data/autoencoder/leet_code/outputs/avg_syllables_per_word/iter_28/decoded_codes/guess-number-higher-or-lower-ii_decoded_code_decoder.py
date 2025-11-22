from math import inf
from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            min_cost = inf
            for pivot in range(left, right + 1):
                cost = pivot + max(dp(left, pivot - 1), dp(pivot + 1, right))
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return dp(1, n)