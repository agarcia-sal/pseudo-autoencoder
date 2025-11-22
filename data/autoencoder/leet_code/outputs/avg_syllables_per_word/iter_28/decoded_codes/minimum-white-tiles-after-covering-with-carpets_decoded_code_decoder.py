from typing import List

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j]: minimum number of white tiles from first i tiles with j carpets used
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                no_cover = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                cover = dp[max(0, i - carpetLen)][j - 1]
                dp[i][j] = min(no_cover, cover)

        return dp[n][numCarpets]