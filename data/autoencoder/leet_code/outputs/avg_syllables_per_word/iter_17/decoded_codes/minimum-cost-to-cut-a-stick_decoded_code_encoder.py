class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]

        from functools import lru_cache

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            minimum_cost = float('inf')
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                if cost < minimum_cost:
                    minimum_cost = cost
            return minimum_cost

        return dp(0, len(cuts) - 1)