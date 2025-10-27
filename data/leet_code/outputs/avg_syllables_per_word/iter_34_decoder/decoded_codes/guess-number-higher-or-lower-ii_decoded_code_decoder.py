import math
from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            min_cost = math.inf
            for pivot in range(left, right + 1):
                left_cost = dp(left, pivot - 1)
                right_cost = dp(pivot + 1, right)
                max_cost = left_cost if left_cost >= right_cost else right_cost
                cost = pivot + max_cost
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return dp(1, n)