from typing import List

class Solution:  
    def hasValidPath(self, grid: List[List[str]]) -> bool:  
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        if n == 0:
            return False

        # If (m + n - 1) is odd, it's impossible to have a valid parentheses sequence
        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j][k] indicates whether it is possible to reach cell (i-1, j-1)
        # with a parenthesis balance of k
        max_k = m + n  # max possible balance + 1
        dp = [[[False] * (max_k + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        # Starting point before any moves (0,1) or (1,0) represents starting at grid[0][0]
        # We initialize dp[0][1][1] = True to simulate having visited (0,0) with balance=1 
        # or dp[1][0][1] = True. But per pseudocode they do dp[0][1][1] = True. We'll follow exactly.
        dp[0][1][1] = True

        for i in range(m):
            for j in range(n):
                for k in range(max_k + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        c = grid[i][j]
                        if c == '(' and k + 1 <= max_k:
                            dp[i + 1][j + 1][k + 1] = True
                        elif c == ')' and k - 1 >= 0:
                            dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]