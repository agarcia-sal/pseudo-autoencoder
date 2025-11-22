class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j] = minimum white tiles in first i tiles with j carpets used
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        # Base case: no carpets used
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # Without using a new carpet covering the i-th tile
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)

                # Using a new carpet ending at i-th tile (cover carpetLen tiles)
                start = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[start][j - 1])

        return dp[n][numCarpets]