from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n + 1
        dp = [[[False] * max_k for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0] = True  # Initialize dp with shifted indices as per pseudocode

        for i in range(m):
            for j in range(n):
                for k in range(max_k):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        if grid[i][j] == '(' and k + 1 < max_k:
                            dp[i + 1][j + 1][k + 1] = True
                        elif grid[i][j] == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]