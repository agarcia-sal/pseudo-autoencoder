class Solution:
    def getMoneyAmount(self, n: int) -> int:
        from math import inf

        memo = {}

        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            min_cost = inf
            for pivot in range(left, right + 1):
                cost = pivot + max(
                    dp(left, pivot - 1),
                    dp(pivot + 1, right)
                )
                if cost < min_cost:
                    min_cost = cost

            memo[(left, right)] = min_cost
            return min_cost

        return dp(1, n)