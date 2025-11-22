from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        number_of_piles = len(piles)
        dp = [[0] * (k + 1) for _ in range(number_of_piles + 1)]

        for i in range(1, number_of_piles + 1):
            current_pile = piles[i - 1]
            for j in range(1, k + 1):
                current_value = 0
                max_coins_to_take = min(j, len(current_pile))
                dp[i][j] = dp[i - 1][j]  # Initialize with not taking any coin from current pile
                for l in range(1, max_coins_to_take + 1):
                    current_value += current_pile[l - 1]
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + current_value)
        return dp[number_of_piles][k]