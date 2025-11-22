class Solution:
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        n = len(floor)
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                dp[i][j] = min(dp[i][j], dp[max(0, i - carpetLen)][j - 1])

        return dp[n][numCarpets]