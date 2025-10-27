class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # If the length of the path is not even, it can't be a valid parentheses string
        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j][k] represents whether it's possible to reach cell (i, j)
        # with a balance of k (number of unmatched '(' parentheses)
        # Dimensions: (m+1) x (n+1) x (m+n+1)
        dp = [[[False] * (m + n + 1) for _ in range(n + 1)] for __ in range(m + 1)]

        dp[0][1][0] = True  # Initialization trick to start from (0,0) properly

        for i in range(m):
            for j in range(n):
                for k in range(m + n + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if grid[i][j] == '(' and k + 1 < m + n + 1:
                            dp[i + 1][j + 1][k + 1] = True
                        elif grid[i][j] == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]