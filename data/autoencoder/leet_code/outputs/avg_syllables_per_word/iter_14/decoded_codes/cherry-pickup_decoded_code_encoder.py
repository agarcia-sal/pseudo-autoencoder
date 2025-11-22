class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0

        # dp[i1][i2][j1] will hold the max cherries collected when
        # first person is at (i1, j1) and second person is at (i2, j2)
        # where j2 = t - i2 (t = i1 + j1 = i2 + j2)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]  # possible step moves: right or down

        for t in range(1, 2 * n - 1):
            # We create a new dp for the current t to avoid overwriting values
            curr_dp = [[-1] * n for _ in range(n)]
            for i1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                j1 = t - i1
                if j1 < 0 or j1 >= n:
                    continue

                for i2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    j2 = t - i2
                    if j2 < 0 or j2 >= n:
                        continue
                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    for di1, dj1 in directions:
                        for di2, dj2 in directions:
                            pi1, pj1 = i1 - di1, j1 - dj1
                            pi2, pj2 = i2 - di2, j2 - dj2
                            if 0 <= pi1 < n and 0 <= pj1 < n and 0 <= pi2 < n and 0 <= pj2 < n:
                                prev = dp[pi1][pi2][pj1]
                                if prev >= 0:
                                    prev_max = max(prev_max, prev)

                    if prev_max < 0:
                        continue

                    cherries = grid[i1][j1]
                    if i1 != i2:
                        cherries += grid[i2][j2]

                    curr_dp[i1][i2] = prev_max + cherries

            dp = curr_dp

        return max(0, dp[n - 1][n - 1])