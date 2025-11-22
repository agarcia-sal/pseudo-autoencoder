from math import inf
from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        length = len(cuts)

        # dp[i][j] will hold the minimum cost to cut between cuts[i] and cuts[j]
        dp = [[0] * length for _ in range(length)]

        # We consider intervals with increasing length
        for interval_length in range(2, length):
            for left in range(length - interval_length):
                right = left + interval_length
                min_cost = inf
                for i in range(left + 1, right):
                    cost = cuts[right] - cuts[left] + dp[left][i] + dp[i][right]
                    if cost < min_cost:
                        min_cost = cost
                dp[left][right] = min_cost

        return dp[0][length - 1]