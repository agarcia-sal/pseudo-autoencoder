class Solution:
    def hasValidPath(self, grid) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        # If the parity of m + n - 1 is odd, can't have a valid parenthesis path
        if (m + n - 1) % 2 != 0:
            return False

        total_length = m + n + 1
        # dp[i][j][k]: can we reach cell (i-1, j-1) with k opened parentheses not yet closed
        dp = [[[False] * total_length for _ in range(n + 1)] for __ in range(m + 1)]
        dp[0][1][0] = True  # initial position outside the grid

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                for k in range(total_length):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if c == '(' and k + 1 < total_length:
                            dp[i + 1][j + 1][k + 1] = True
                        elif c == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]