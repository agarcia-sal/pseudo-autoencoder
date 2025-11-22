from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        dp = self.initialize_2d_list(m, n)

        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]

    def initialize_2d_list(self, m: int, n: int) -> List[List[int]]:
        result = []
        for _ in range(m):
            row = [0] * n
            result.append(row)
        return result