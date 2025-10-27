from math import inf
from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        if n == 1:
            return min(grid[0])

        dp = grid[0][:]

        for i in range(1, n):
            new_dp = [0] * n
            min1, min2 = inf, inf
            min1_index = -1

            for j in range(n):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    min1_index = j
                elif dp[j] < min2:
                    min2 = dp[j]

            for j in range(n):
                if j == min1_index:
                    new_dp[j] = grid[i][j] + min2
                else:
                    new_dp[j] = grid[i][j] + min1

            dp = new_dp[:]

        return min(dp)