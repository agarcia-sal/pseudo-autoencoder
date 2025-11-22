from functools import lru_cache
from math import inf

class Solution:
    def minCost(self, n, cuts):
        cuts = sorted([0] + cuts + [n])

        @lru_cache(None)
        def dp(left, right):
            if right - left <= 1:
                return 0

            min_cost = inf
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return dp(0, len(cuts) - 1)