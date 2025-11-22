class Solution:
    def getMoneyAmount(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            minimum_cost = float('inf')
            for pivot in range(left, right + 1):
                cost_to_consider = pivot + max(dp(left, pivot - 1), dp(pivot + 1, right))
                minimum_cost = min(minimum_cost, cost_to_consider)
            return minimum_cost

        return dp(1, n)