class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize dp with 1s, as there's exactly one way to reach any cell in first row or column
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]