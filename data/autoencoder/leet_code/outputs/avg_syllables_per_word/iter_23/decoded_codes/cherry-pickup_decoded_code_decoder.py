from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n-1][n-1] == -1:
            return 0

        # dp[i1][i2][j1] stores the max cherries collected when first person is at (i1, j1)
        # and second person is at (i2, j2), where j2 = (i1 + j1) - (i2) = t - i2
        dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0,1), (1,0)]

        for t in range(1, 2*n - 1):
            # We traverse i1 and i2 within the feasible range for the current step t
            new_dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
            start = max(0, t - (n-1))
            end = min(n, t + 1)
            for i1 in range(start, end):
                for i2 in range(start, end):
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
                    if prev_max >= 0:
                        cherries = grid[i1][j1] if i1 == i2 else grid[i1][j1] + grid[i2][j2]
                        new_dp[i1][i2][j1] = prev_max + cherries
            dp = new_dp

        return max(0, dp[n-1][n-1][n-1])