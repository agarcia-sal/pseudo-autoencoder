from math import inf

class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # Precompute cost[i][j]: minimum cost to cover houses[i..j] with one mailbox
        cost = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]