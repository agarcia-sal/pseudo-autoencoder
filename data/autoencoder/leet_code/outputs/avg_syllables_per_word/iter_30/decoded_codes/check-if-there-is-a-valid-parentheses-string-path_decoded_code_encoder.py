from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        max_balance = m + n + 1
        # dp dimensions: (m+1) x (n+1) x max_balance
        # Use a 3D list initialized with False
        dp = [[[False] * max_balance for _ in range(n + 1)] for __ in range(m + 1)]
        dp[0][1][0] = True  # offset by 1 to handle initial position (0,0) in dp indexing
        for i in range(m):
            for j in range(n):
                for k in range(max_balance):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        c = grid[i][j]
                        if c == '(' and k + 1 < max_balance:
                            dp[i + 1][j + 1][k + 1] = True
                        elif c == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True
        return dp[m][n][0]