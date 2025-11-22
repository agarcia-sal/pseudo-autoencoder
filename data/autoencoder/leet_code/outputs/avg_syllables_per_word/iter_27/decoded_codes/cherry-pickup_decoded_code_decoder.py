from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0

        # dp[i1][i2][t - i1] represents the maximum cherries collected up to step t
        # where first person is at (i1, j1) and second person is at (i2, j2) with j1 = t - i1, j2 = t - i2
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]

        for t in range(1, 2 * n - 1):
            # We create a new dp for step t to avoid overwriting previous steps prematurely
            new_dp = [[-1] * n for _ in range(n)]
            start = max(0, t - (n - 1))
            end = min(n, t + 1)
            for i1 in range(start, end):
                j1 = t - i1
                if j1 >= n or j1 < 0:
                    continue
                for i2 in range(start, end):
                    j2 = t - i2
                    if j2 >= n or j2 < 0:
                        continue
                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    for di1, dj1 in directions:
                        pi1, pj1 = i1 - di1, j1 - dj1
                        if not (0 <= pi1 < n and 0 <= pj1 < n):
                            continue
                        for di2, dj2 in directions:
                            pi2, pj2 = i2 - di2, j2 - dj2
                            if not (0 <= pi2 < n and 0 <= pj2 < n):
                                continue
                            prev = dp[pi1][pi2][pj1]
                            if prev >= 0 and prev > prev_max:
                                prev_max = prev

                    if prev_max < 0:
                        continue

                    cherries = grid[i1][j1]
                    if i1 != i2:
                        cherries += grid[i2][j2]

                    if prev_max + cherries > new_dp[i1][i2]:
                        new_dp[i1][i2] = prev_max + cherries
            dp = new_dp

        return max(0, dp[n - 1][n - 1])