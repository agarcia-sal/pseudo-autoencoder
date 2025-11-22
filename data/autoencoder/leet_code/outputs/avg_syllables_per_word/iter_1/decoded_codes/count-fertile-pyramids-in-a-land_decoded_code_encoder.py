def countPyramids(grid):
    def top():
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or j == 0 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + 1
                    if dp[i][j] > 1:
                        c += dp[i][j] - 1
        return c

    def bottom():
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        c = 0
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == m - 1 or j == 0 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1]) + 1
                    if dp[i][j] > 1:
                        c += dp[i][j] - 1
        return c

    return top() + bottom()