from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            current_pile = piles[i - 1]
            prefix_sum = [0]
            for coin in current_pile:
                prefix_sum.append(prefix_sum[-1] + coin)

            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]  # initialize dp[i][j] to not taking any coins from current pile
                max_l = min(j, len(current_pile))
                for l in range(1, max_l + 1):
                    candidate = dp[i - 1][j - l] + prefix_sum[l]
                    if candidate > dp[i][j]:
                        dp[i][j] = candidate

        return dp[n][k]