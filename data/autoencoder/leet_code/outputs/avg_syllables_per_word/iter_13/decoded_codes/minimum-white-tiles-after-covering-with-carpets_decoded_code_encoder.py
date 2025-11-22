class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j] = minimum white tiles from first i tiles using j carpets
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                without_carpet = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                with_carpet = dp[max(0, i - carpetLen)][j - 1]
                dp[i][j] = min(without_carpet, with_carpet)

        return dp[n][numCarpets]