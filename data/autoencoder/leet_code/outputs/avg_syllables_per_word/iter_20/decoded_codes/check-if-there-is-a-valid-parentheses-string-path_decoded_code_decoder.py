from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j][k] indicates whether there is a valid path to (i,j)
        # with k open parentheses not yet closed
        # Dimensions: (m+1) x (n+1) x (m+n+1)
        # Use a 3D boolean array initialized as False
        dp = [[[False] * (m + n + 1) for _ in range(n + 1)] for __ in range(m + 1)]

        # Starting state: before any cells visited (at dp[0][1][0] per pseudocode)
        # Carefully matching the pseudocode:
        # "SET element at position zero of list at position one of list at position zero of dp TO true"
        # dp[0][1][0] = True
        dp[0][1][0] = True

        for i in range(m):
            for j in range(n):
                for k in range(m + n + 1):
                    # Check if dp[i][j+1][k] or dp[i+1][j][k] is True (from pseudocode: 
                    # "IF element at position j plus one of list at position i of dp IS true OR 
                    #  element at position j of list at position i plus one of dp IS true")
                    # Then update dp[i+1][j+1][k +/- 1] depending on grid[i][j]
                    if j + 1 <= n and dp[i][j + 1][k]:
                        cell = grid[i][j]
                        if cell == '(':
                            if k + 1 < m + n + 1:
                                dp[i + 1][j + 1][k + 1] = True
                        elif cell == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True
                    if i + 1 <= m and dp[i + 1][j][k]:
                        cell = grid[i][j]
                        if cell == '(':
                            if k + 1 < m + n + 1:
                                dp[i + 1][j + 1][k + 1] = True
                        elif cell == ')':
                            if k - 1 >= 0:
                                dp[i + 1][j + 1][k - 1] = True

        return dp[m][n][0]