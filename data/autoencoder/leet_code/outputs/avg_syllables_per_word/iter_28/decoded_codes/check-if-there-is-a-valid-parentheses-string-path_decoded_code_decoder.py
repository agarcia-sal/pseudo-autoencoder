from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n
        # dp dimensions: (m+1) x (n+1) x (max_k+1)
        # dp[i][j][k] means at position (i-1, j-1) in grid,
        # with k opened parentheses (k >= 0), can we reach this state?
        dp = [[[False] * (max_k + 1) for _ in range(n + 1)] for __ in range(m + 1)]
        dp[1][0][0] = True  # Start before (0,0)

        for i in range(m):
            for j in range(n):
                for k in range(max_k + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        c = grid[i][j]
                        if c == '(':
                            if k + 1 <= max_k:
                                dp[i + 1][j + 1][k + 1] = True
                        elif c == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]