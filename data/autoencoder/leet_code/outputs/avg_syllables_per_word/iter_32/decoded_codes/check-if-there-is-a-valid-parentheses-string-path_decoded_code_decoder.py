from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        # If (m + n - 1) is odd, it's impossible to have a balanced parentheses path
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n + 1  # maximum stack size for dp dimension k

        # dp[i][j][k] = True if a valid parentheses path reaches cell (i-1, j-1) with balance k
        # dimensions: (m+1) x (n+1) x (max_k)
        dp = [[[False] * max_k for _ in range(n + 1)] for __ in range(m + 1)]
        dp[0][1][0] = True  # offset start: from dp[0][1] and dp[1][0], so dp[0][1][0] is starting point (0,0)

        for i in range(m):
            for j in range(n):
                for k in range(max_k):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        c = grid[i][j]
                        if c == '(' and k + 1 < max_k:
                            dp[i + 1][j + 1][k + 1] = True
                        elif c == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]