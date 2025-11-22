from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n-1][n-1] == -1:
            return 0

        dp = self.initialize_dp_table(n)
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]

        for t in range(1, 2 * n - 1):
            # Prepare a new dp layer to avoid overwriting in-place
            new_dp = [[[-1] * n for _ in range(n)] for __ in range(n)]
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
                        pi1, pj1 = i1 - di1, j1 - dj1
                        if not (0 <= pi1 < n and 0 <= pj1 < n):
                            continue
                        for di2, dj2 in directions:
                            pi2, pj2 = i2 - di2, j2 - dj2
                            if not (0 <= pi2 < n and 0 <= pj2 < n):
                                continue
                            if dp[pi1][pi2][pj1] >= 0:
                                prev_max = max(prev_max, dp[pi1][pi2][pj1])

                    if prev_max >= 0:
                        if i1 == i2:
                            cherries = grid[i1][j1]
                        else:
                            cherries = grid[i1][j1] + grid[i2][j2]
                        new_dp[i1][i2][j1] = prev_max + cherries
            dp = new_dp

        return max(0, dp[n - 1][n - 1][n - 1])

    def initialize_dp_table(self, n: int) -> List[List[List[int]]]:
        return [[[-1] * n for _ in range(n)] for __ in range(n)]