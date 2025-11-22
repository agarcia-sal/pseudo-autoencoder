from typing import List

class Solution:
    def minimumWhiteTiles(self, floor: List[int], numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            pos = i - 1
            dp[i][0] = dp[i - 1][0] + (1 if floor[pos] == 1 else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                pos = i - 1
                option_one = dp[i - 1][j] + (1 if floor[pos] == 1 else 0)
                carpet_start = i - carpetLen
                if carpet_start < 0:
                    carpet_start = 0
                option_two = dp[carpet_start][j - 1]
                dp[i][j] = option_one if option_one < option_two else option_two

        return dp[n][numCarpets]