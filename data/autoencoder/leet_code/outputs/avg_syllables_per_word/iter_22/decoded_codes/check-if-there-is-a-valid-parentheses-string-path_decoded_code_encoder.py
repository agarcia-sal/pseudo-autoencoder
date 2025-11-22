class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # If (m + n - 1) is odd, no valid path is possible
        if (m + n - 1) % 2 != 0:
            return False

        # dp dimensions: (m+1) x (n+1) x (m+n+1), default False
        dp = [[[False] * (m + n + 1) for _ in range(n + 1)] for __ in range(m + 1)]

        dp[0][1][0] = True  # Initialization as per pseudocode

        for i in range(m):
            for j in range(n):
                for k in range(m + n + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        char = grid[i][j]
                        if char == '(' and k + 1 < m + n + 1:
                            dp[i + 1][j + 1][k + 1] = True
                        elif char == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]