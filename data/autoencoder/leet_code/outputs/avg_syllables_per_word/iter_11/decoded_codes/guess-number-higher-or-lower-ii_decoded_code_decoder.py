class Solution:
    def getMoneyAmount(self, n: int) -> int:
        from functools import cache

        @cache
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            min_cost = float('inf')
            for pivot in range(left, right + 1):
                cost = pivot + max(dp(left, pivot - 1), dp(pivot + 1, right))
                min_cost = min(min_cost, cost)
            return min_cost

        return dp(1, n)