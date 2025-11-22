from typing import List

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j]: minimum white tiles remaining in first i tiles with j carpets used
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                white_tile = 1 if floor[i - 1] == '1' else 0
                # Case 1: no new carpet placed at current tile
                dp[i][j] = dp[i - 1][j] + white_tile
                # Case 2: place a carpet ending at current tile covering carpetLen tiles
                start_idx = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[start_idx][j - 1])

        return dp[n][numCarpets]