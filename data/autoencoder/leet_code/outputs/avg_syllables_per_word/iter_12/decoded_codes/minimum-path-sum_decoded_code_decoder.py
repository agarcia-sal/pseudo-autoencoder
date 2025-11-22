class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        dp = self.create_2D_list_of_zeros(m, n)

        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]

        return dp[m-1][n-1]

    def create_2D_list_of_zeros(self, rows, columns):
        return [[0 for _ in range(columns)] for _ in range(rows)]