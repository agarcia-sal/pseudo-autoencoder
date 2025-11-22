from math import inf
from functools import lru_cache

class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if cuts[right] - cuts[left] <= 1:
                return 0
            min_cost = inf
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return dp(0, len(cuts) - 1)