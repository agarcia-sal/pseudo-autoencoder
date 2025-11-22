class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]

        # Precompute cost[i][j]: minimal total distance to cover houses[i..j] with one mailbox
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                median = houses[(i + j) // 2]
                total = 0
                for m in range(i, j + 1):
                    total += abs(houses[m] - median)
                cost[i][j] = total

        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]