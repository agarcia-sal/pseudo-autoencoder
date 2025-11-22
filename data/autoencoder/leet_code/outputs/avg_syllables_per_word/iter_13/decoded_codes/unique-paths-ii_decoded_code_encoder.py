class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for col in range(1, n):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]

        for row in range(1, m):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]