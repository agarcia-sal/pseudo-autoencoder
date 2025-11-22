class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n
        dp = [[[False] * (max_k + 1) for _ in range(n + 1)] for __ in range(m + 1)]
        dp[0][1][0] = True

        for i in range(m):
            for j in range(n):
                for k in range(max_k + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if grid[i][j] == '(' and k + 1 <= max_k:
                            dp[i + 1][j + 1][k + 1] = True
                        elif grid[i][j] == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]