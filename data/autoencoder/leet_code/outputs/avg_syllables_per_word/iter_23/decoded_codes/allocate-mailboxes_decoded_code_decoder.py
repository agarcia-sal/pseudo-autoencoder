from math import inf
from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # Precompute cost[i][j]: min total distance to cover houses[i..j] with one mailbox
        cost = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        # dp[i][j]: minimum total distance to cover first i houses with j mailboxes
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0.0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    val = dp[p][j - 1] + cost[p][i - 1]
                    if val < dp[i][j]:
                        dp[i][j] = val

        return int(dp[n][k])