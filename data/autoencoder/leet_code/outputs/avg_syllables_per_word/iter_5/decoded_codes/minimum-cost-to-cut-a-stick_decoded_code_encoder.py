from functools import cache

class Solution:
    def minCost(self, n, cuts):
        cuts = [0] + sorted(cuts) + [n]

        @cache
        def dp(left, right):
            if right - left <= 1:
                return 0
            min_cost = float('inf')
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return dp(0, len(cuts) - 1)