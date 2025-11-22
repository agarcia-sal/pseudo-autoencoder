from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = self.createTwoDimensionalList(m, n)

        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                minimum_predecessor = min(dp[i-1][j], dp[i][j-1])
                dp[i][j] = minimum_predecessor + grid[i][j]

        return dp[m-1][n-1]

    def createTwoDimensionalList(self, row_count: int, column_count: int) -> List[List[int]]:
        return [[0] * column_count for _ in range(row_count)]