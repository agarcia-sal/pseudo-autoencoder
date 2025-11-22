from math import inf

class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = sorted([0] + cuts + [n])

        def dp(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            minimum_cost = inf
            for index in range(left + 1, right):
                current_cost = cuts[right] - cuts[left] + dp(left, index) + dp(index, right)
                if current_cost < minimum_cost:
                    minimum_cost = current_cost
            return minimum_cost

        return dp(0, len(cuts) - 1)