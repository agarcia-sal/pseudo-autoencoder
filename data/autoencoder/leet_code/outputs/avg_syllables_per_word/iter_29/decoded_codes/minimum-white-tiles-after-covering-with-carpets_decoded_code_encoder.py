class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j]: minimum white tiles uncovered in first i tiles using j carpets
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (floor[i - 1] == '1')

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + (floor[i - 1] == '1')
                start = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[start][j - 1])

        return dp[n][numCarpets]