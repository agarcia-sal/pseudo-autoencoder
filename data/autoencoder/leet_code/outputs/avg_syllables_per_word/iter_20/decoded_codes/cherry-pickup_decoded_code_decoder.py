class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0

        dp = [[[-1] * n for _ in range(n)] for __ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]

        for t in range(1, 2 * n - 1):
            # Temporary dp for current step to avoid overwriting needed data in dp during iteration
            curr_dp = [[-1] * n for _ in range(n)]
            imin = max(0, t - (n - 1))
            imax = min(n, t + 1)
            for i1 in range(imin, imax):
                j1 = t - i1
                if j1 < 0 or j1 >= n:
                    continue

                for i2 in range(imin, imax):
                    j2 = t - i2
                    if j2 < 0 or j2 >= n:
                        continue

                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    for di1, dj1 in directions:
                        pi1 = i1 - di1
                        pj1 = j1 - dj1
                        if not (0 <= pi1 < n and 0 <= pj1 < n):
                            continue
                        for di2, dj2 in directions:
                            pi2 = i2 - di2
                            pj2 = j2 - dj2
                            if not (0 <= pi2 < n and 0 <= pj2 < n):
                                continue
                            val = dp[pi1][pi2][pj1]
                            if val > prev_max:
                                prev_max = val

                    if prev_max >= 0:
                        if i1 == i2:
                            cherries = grid[i1][j1]
                        else:
                            cherries = grid[i1][j1] + grid[i2][j2]
                        curr_dp[i1][i2] = prev_max + cherries
            dp = curr_dp

        return max(0, dp[n - 1][n - 1])