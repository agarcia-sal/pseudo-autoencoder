from typing import List
import math
import copy

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0

        n = len(grid)

        if n == 1:
            return min(grid[0])

        dp = copy.copy(grid[0])

        for i in range(1, n):
            new_dp = [0] * n
            min1 = math.inf
            min2 = math.inf
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

            dp = copy.copy(new_dp)

        return min(dp)