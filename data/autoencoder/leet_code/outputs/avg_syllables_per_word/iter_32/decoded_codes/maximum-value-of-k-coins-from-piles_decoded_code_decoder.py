from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # dp[i][j] = max value using first i piles and taking j coins in total
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            current_pile = piles[i - 1]
            prefix_sum = [0]
            for coin_value in current_pile:
                prefix_sum.append(prefix_sum[-1] + coin_value)
            length = len(current_pile)
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]  # take 0 coins from current pile
                # try taking l coins from current pile
                for l in range(1, min(j, length) + 1):
                    # dp[i-1][j-l] + sum of first l coins from current pile
                    cand = dp[i - 1][j - l] + prefix_sum[l]
                    if cand > dp[i][j]:
                        dp[i][j] = cand
        return dp[n][k]