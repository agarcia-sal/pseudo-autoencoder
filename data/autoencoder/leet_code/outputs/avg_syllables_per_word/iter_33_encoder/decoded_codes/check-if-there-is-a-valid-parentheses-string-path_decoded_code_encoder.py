class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # The path length = m + n - 1 must be even to have a valid parentheses string
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n  # max length of the path + 1 for dp indexing
        # dp[i][j][k]: if there's a path to (i-1, j-1) with k open parentheses count
        dp = [[[False] * (max_k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][0][0] = True  # Starting from (0,0) with 0 open parentheses count

        for i in range(m):
            for j in range(n):
                ch = grid[i][j]
                for k in range(max_k + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if ch == '(':
                            if k + 1 <= max_k:
                                dp[i + 1][j + 1][k + 1] = True
                        elif ch == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True

        # Check if there's a valid path ending at bottom-right corner with zero open parentheses
        return dp[m][n][0]