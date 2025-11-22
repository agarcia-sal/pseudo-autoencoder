from typing import List

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp: List[List[int]] = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                prev_index = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[prev_index][j - 1])

        return dp[n][numCarpets]