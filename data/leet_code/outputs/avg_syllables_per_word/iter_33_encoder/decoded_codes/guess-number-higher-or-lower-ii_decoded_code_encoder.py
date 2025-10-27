class Solution:
    def getMoneyAmount(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            minimum_cost = float('inf')
            for pivot in range(left, right + 1):
                left_cost = dp(left, pivot - 1)
                right_cost = dp(pivot + 1, right)
                cost = pivot + max(left_cost, right_cost)
                minimum_cost = min(minimum_cost, cost)
            return minimum_cost

        return dp(1, n)