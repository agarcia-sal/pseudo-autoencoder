class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        dp = self.dp_initialization(m + 1, n + 1, m + n + 1)
        dp[0][1][0] = True

        for i in range(m):
            for j in range(n):
                for k in range(m + n):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if grid[i][j] == '(':
                            if k + 1 < m + n + 1:
                                dp[i + 1][j + 1][k + 1] = True
                        elif grid[i][j] == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]

    def dp_initialization(self, rows, columns, depth):
        return [[[False] * depth for _ in range(columns)] for _ in range(rows)]