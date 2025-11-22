from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        # If path length (m+n-1) is odd, cannot have valid parentheses sequence
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n  # maximum parentheses balance
        # dp[i][j][k] = True if there's a path to cell (i,j) with k '(' more than ')'
        # Dimensions: (m+1) x (n+1) x (max_k+1)
        dp = [[[False] * (max_k + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        # Base case, start from dp[0][1][0] = True (dp indices are offset to allow access at dp[i+1][j] etc.)
        dp[0][1][0] = True

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                for k in range(max_k + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if c == '(':
                            if k + 1 <= max_k:
                                dp[i + 1][j + 1][k + 1] = True
                        elif c == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]