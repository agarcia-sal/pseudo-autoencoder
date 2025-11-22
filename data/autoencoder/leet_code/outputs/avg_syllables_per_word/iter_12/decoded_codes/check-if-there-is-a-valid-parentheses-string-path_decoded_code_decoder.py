class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        # If the length of path (m + n - 1) is odd, can't form valid parentheses sequence
        if (m + n - 1) % 2 != 0:
            return False

        dp = self.initialize_dp(m + 1, n + 1, m + n + 1)
        dp[1][0][0] = True

        for i in range(m):
            for j in range(n):
                for k in range(m + n):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if grid[i][j] == '(' and k + 1 < m + n + 1:
                            dp[i + 1][j + 1][k + 1] = True
                        elif grid[i][j] == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]

    def initialize_dp(self, dim1, dim2, dim3):
        # Create a 3D list with dimensions dim1 x dim2 x dim3, filled with False
        return [[[False] * dim3 for _ in range(dim2)] for __ in range(dim1)]