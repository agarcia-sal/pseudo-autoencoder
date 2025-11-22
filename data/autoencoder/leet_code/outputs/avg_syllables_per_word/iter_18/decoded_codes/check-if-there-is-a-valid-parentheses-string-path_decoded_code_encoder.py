from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j][k]: boolean indicating if it's possible to reach cell (i, j)
        # with k unmatched opening parentheses along the path.
        dp = [[[False] * (m + n + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0] = True  # initialization to align with the pseudocode indexing

        for i in range(m):
            for j in range(n):
                for k in range(m + n + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        ch = grid[i][j]
                        if ch == '(' and k + 1 < m + n + 1:
                            dp[i + 1][j + 1][k + 1] = True
                        elif ch == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]