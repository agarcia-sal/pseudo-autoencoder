from math import inf

class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        memo = {}

        def dp(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            min_cost = inf
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                if cost < min_cost:
                    min_cost = cost
            memo[(left, right)] = min_cost
            return min_cost

        return dp(0, len(cuts) - 1)