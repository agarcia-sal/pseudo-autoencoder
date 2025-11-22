from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            current_pile = piles[i - 1]
            for j in range(1, k + 1):
                current_value = 0
                dp[i][j] = dp[i - 1][j]
                for l in range(1, min(j, len(current_pile)) + 1):
                    current_value += current_pile[l - 1]
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + current_value)

        return dp[n][k]