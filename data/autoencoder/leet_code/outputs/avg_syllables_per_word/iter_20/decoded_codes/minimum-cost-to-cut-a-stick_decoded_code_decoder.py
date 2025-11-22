from math import inf
from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        length = len(cuts)

        from functools import lru_cache

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if right - left <= 1:
                return 0

            min_cost = inf
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                if cost < min_cost:
                    min_cost = cost

            return min_cost

        return dp(0, length - 1)