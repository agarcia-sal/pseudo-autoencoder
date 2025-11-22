from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        reference = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 2):
            for i in range(0, n + 2 - length):
                j = i + length
                for k in range(i + 1, j):
                    coins = reference[i] * reference[k] * reference[j] + dp[i][k] + dp[k][j]
                    if coins > dp[i][j]:
                        dp[i][j] = coins

        return dp[0][n + 1]