from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize dp array with 1s
        dp = [[1] * n for _ in range(m)]

        # Compute number of paths for each cell by summing top and left cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Return number of unique paths to bottom-right corner
        return dp[m-1][n-1]