class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]