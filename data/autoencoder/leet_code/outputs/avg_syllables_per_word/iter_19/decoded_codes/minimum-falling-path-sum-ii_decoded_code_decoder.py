from math import inf
from copy import copy

class Solution:
    def minFallingPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        if n == 1:
            return min(grid[0])

        dp = copy(grid[0])
        for i in range(1, n):
            new_dp = [0] * n
            min1 = inf
            min2 = inf
            min1_index = -1

            for j in range(n):
                val = dp[j]
                if val < min1:
                    min2 = min1
                    min1 = val
                    min1_index = j
                elif val < min2:
                    min2 = val

            for j in range(n):
                if j == min1_index:
                    new_dp[j] = grid[i][j] + min2
                else:
                    new_dp[j] = grid[i][j] + min1

            dp = copy(new_dp)

        return min(dp)