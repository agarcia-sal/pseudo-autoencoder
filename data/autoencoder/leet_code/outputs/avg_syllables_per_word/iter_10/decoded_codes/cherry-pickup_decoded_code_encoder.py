class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        if grid[0][0] == -1 or grid[n-1][n-1] == -1:
            return 0

        dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0,1), (1,0)]

        for t in range(1, 2*n - 1):
            for i1 in range(max(0, t-(n-1)), min(n, t+1)):
                for i2 in range(max(0, t-(n-1)), min(n, t+1)):
                    j1, j2 = t - i1, t - i2
                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    for di1, dj1 in directions:
                        pi1, pj1 = i1 - di1, j1 - dj1
                        if pi1 < 0 or pj1 < 0 or pi1 >= n or pj1 >= n:
                            continue
                        for di2, dj2 in directions:
                            pi2, pj2 = i2 - di2, j2 - dj2
                            if pi2 < 0 or pj2 < 0 or pi2 >= n or pj2 >= n:
                                continue
                            if dp[pi1][pi2][pj1] >= 0:
                                prev_max = max(prev_max, dp[pi1][pi2][pj1])
                    if prev_max < 0:
                        continue

                    cherries = grid[i1][j1] if i1 == i2 else grid[i1][j1] + grid[i2][j2]
                    dp[i1][i2][j1] = prev_max + cherries

        return max(0, dp[n-1][n-1][n-1])