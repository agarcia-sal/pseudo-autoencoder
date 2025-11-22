from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        if n == 0:
            return False

        # Early pruning: if (m + n - 1) is odd, no valid parentheses path exists
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n  # maximum possible parentheses depth + 1

        # Initialize 3D DP array: dp[i][j][k] = bool
        # Using list comprehension for efficiency and clarity
        dp = [[[False] * max_k for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0] = True  # Starting position before entering grid (i=0, j=0)

        for i in range(m):
            for j in range(n):
                for k in range(max_k):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        c = grid[i][j]
                        if c == '(':
                            if k + 1 < max_k:
                                dp[i + 1][j + 1][k + 1] = True
                        elif c == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True
        return dp[m][n][0]