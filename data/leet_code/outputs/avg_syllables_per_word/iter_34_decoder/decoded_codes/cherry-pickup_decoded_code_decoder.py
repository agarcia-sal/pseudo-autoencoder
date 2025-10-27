from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0

        # dp[i1][i2][j1] represents max cherries collected when 
        # first person is at (i1, j1) and second person is at (i2, j2)
        # with t = i1 + j1 = i2 + j2, so j2 = t - i2
        dp = [[[-1] * n for _ in range(n)] for __ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]
        for t in range(1, 2 * n - 1):
            # Because i1 + j1 = t and i2 + j2 = t,
            # i1 and i2 are the row indices and range accordingly
            for i1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                for i2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    j1 = t - i1
                    j2 = t - i2
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
                                if dp[pi1][pi2][pj1] > prev_max:
                                    prev_max = dp[pi1][pi2][pj1]

                    if prev_max >= 0:
                        if i1 == i2:
                            cherries = grid[i1][j1]
                        else:
                            cherries = grid[i1][j1] + grid[i2][j2]
                        dp[i1][i2][j1] = prev_max + cherries

        return max(0, dp[n - 1][n - 1][n - 1])