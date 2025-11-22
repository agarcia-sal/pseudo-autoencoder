from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n-1][n-1] == -1:
            return 0

        dp = self.InitializeDPTable(n)
        dp[0][0][0] = grid[0][0]
        directions = self.GetDirections()

        for t in range(1, 2 * n):
            start = max(0, t - (n - 1))
            end = min(n, t + 1)
            for i1 in range(start, end):
                for i2 in range(start, end):
                    j1 = t - i1
                    j2 = t - i2
                    if j1 >= n or j2 >= n:
                        continue
                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    for d1 in directions:
                        for d2 in directions:
                            pi1, pj1 = i1 - d1[0], j1 - d1[1]
                            pi2, pj2 = i2 - d2[0], j2 - d2[1]
                            if 0 <= pi1 < n and 0 <= pj1 < n and 0 <= pi2 < n and 0 <= pj2 < n:
                                prev_max = max(prev_max, dp[pi1][pi2][pj1])
                    if prev_max < 0:
                        continue

                    if i1 == i2:
                        cherries = grid[i1][j1]
                    else:
                        cherries = grid[i1][j1] + grid[i2][j2]

                    dp[i1][i2][j1] = prev_max + cherries

        return max(0, dp[n-1][n-1][n-1])

    def InitializeDPTable(self, n: int) -> List[List[List[int]]]:
        # 3D DP table n x n x n filled with -1
        return [[[-1] * n for _ in range(n)] for __ in range(n)]

    def GetDirections(self) -> List[List[int]]:
        # Directions for right and down moves
        return [[0, 1], [1, 0]]