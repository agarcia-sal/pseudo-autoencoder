from math import inf

class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = sorted(cuts + [0, n])

        from functools import lru_cache

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            min_cost = inf
            for index in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, index) + dp(index, right)
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return dp(0, len(cuts) - 1)