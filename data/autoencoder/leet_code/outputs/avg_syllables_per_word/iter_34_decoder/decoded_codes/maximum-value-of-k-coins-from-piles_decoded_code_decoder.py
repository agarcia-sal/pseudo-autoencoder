from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # dp[i][j]: max value taking from first i piles with j coins
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            current_pile = piles[i - 1]
            for j in range(1, k + 1):
                current_value = 0
                # try taking l coins from current pile
                for l in range(min(j, len(current_pile)) + 1):
                    if l > 0:
                        current_value += current_pile[l - 1]
                    if dp[i][j] < dp[i - 1][j - l] + current_value:
                        dp[i][j] = dp[i - 1][j - l] + current_value

        return dp[n][k]