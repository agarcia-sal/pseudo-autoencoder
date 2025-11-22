from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0

        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]

        for t in range(1, 2 * n - 1):
            # Temporary 3D dp for current t to avoid overwrite during iteration
            curr_dp = [[-1] * n for _ in range(n)]
            for i1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                for i2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    j1 = t - i1
                    j2 = t - i2
                    if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
                        continue
                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    for di1, dj1 in directions:
                        for di2, dj2 in directions:
                            pi1 = i1 - di1
                            pj1 = j1 - dj1
                            pi2 = i2 - di2
                            pj2 = j2 - dj2
                            if 0 <= pi1 < n and 0 <= pj1 < n and 0 <= pi2 < n and 0 <= pj2 < n:
                                if dp[pi1][pi2][pj1] >= 0:
                                    prev_max = max(prev_max, dp[pi1][pi2][pj1])
                    if prev_max < 0:
                        continue

                    cherries = grid[i1][j1] if i1 == i2 else grid[i1][j1] + grid[i2][j2]
                    curr_dp[i1][i2] = prev_max + cherries

            # Update dp to current dp layer
            for i1 in range(n):
                for i2 in range(n):
                    dp[i1][i2][:] = [-1] * n  # reset last dimension first
            for i1 in range(n):
                for i2 in range(n):
                    dp[i1][i2][:] = [-1] * n
            for i1 in range(n):
                for i2 in range(n):
                    dp[i1][i2][t - i1 if 0 <= t - i1 < n else 0] = curr_dp[i1][i2]
            # But the above approach is incorrect; we must assign dp[i1][i2][j1] correctly

            # Correcting dimension update:
            # dp[i1][i2][j1] = curr_dp[i1][i2] where j1 = t - i1
            # We must reset dp to -1, then only set these positions.

            # Rebuild dp with -1:
            dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
            for i1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                for i2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    j1 = t - i1
                    if 0 <= j1 < n:
                        dp[i1][i2][j1] = curr_dp[i1][i2]

        return max(0, dp[n - 1][n - 1][n - 1])