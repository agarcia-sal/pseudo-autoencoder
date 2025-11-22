class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        # If path length is not even, it's impossible to have a valid parenthesis path
        if (m + n - 1) % 2 != 0:
            return False

        max_open = m + n  # max possible open parentheses count
        # dp[i][j][k] = True if we can reach cell (i,j) with k open parentheses count
        dp = [[[False] * (max_open + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][1][0] = True  # initialize to true for dp[0][1][0] as per pseudocode

        for i in range(m):
            for j in range(n):
                for k in range(max_open + 1):
                    # Check states from top or left cells with same count k
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if grid[i][j] == '(' and k + 1 <= max_open:
                            dp[i + 1][j + 1][k + 1] = True
                        elif grid[i][j] == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]