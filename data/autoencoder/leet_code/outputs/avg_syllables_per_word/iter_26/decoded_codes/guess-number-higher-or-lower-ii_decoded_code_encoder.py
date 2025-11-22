from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            minimal_cost = float('inf')
            for pivot in range(left, right + 1):
                cost_value = pivot + max(dp(left, pivot - 1), dp(pivot + 1, right))
                minimal_cost = min(minimal_cost, cost_value)
            return minimal_cost

        return dp(1, n)