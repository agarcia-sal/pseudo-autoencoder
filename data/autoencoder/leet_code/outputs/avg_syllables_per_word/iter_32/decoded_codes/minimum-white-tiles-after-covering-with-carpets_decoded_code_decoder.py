from typing import List

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j]: minimum white tiles remaining when covering first i tiles with j carpets
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        # Base case: no carpets used, count white tiles up to i
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # Case 1: do not cover i-th tile with current carpet
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)

                # Case 2: cover last carpetLen tiles with current carpet
                left = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[left][j - 1])

        return dp[n][numCarpets]