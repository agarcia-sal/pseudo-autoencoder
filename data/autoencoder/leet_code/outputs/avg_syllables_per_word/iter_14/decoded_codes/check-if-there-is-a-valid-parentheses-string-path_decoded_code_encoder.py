class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        # If the total steps (m + n - 1) is odd, can't have balanced parentheses
        if (m + n - 1) % 2 != 0:
            return False

        max_k = m + n
        # Initialize 3D DP array with False, dimensions: (m+1) x (n+1) x (max_k+1)
        dp = [[[False] * (max_k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0] = True  # Base case initialization

        for i in range(m):
            for j in range(n):
                for k in range(max_k + 1):
                    if dp[i][j + 1][k] or dp[i + 1][j][k]:
                        ch = grid[i][j]
                        if ch == '(':
                            nk = k + 1
                            if nk <= max_k:
                                dp[i + 1][j + 1][nk] = True
                        else:  # ch == ')'
                            nk = k - 1
                            if nk >= 0:
                                dp[i + 1][j + 1][nk] = True

        return dp[m][n][0]