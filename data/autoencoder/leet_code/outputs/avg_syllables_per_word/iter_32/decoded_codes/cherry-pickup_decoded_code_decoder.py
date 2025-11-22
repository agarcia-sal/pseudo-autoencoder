from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # If start or end positions are blocked, return 0 immediately
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0

        # dp[i1][i2][j1] where:
        # i1, j1 are coordinates of first person (row and col),
        # i2, j2 are coordinates of second person, with j2 = i1 + j1 - i2 (since t = i1+j1 = i2+j2)
        # But here dp is 3D since j2 can be derived from t - i2
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        directions = [(0, 1), (1, 0)]  # moves: right or down

        max_t = 2 * n - 2  # max steps from (0,0) to (n-1,n-1)

        for t in range(1, max_t + 1):
            # i1 iterates over possible rows for person1 such that j1 = t - i1 is valid
            for i1 in range(max(0, t - (n - 1)), min(n, t + 1)):
                j1 = t - i1
                if j1 < 0 or j1 >= n:
                    continue
                for i2 in range(max(0, t - (n - 1)), min(n, t + 1)):
                    j2 = t - i2
                    if j2 < 0 or j2 >= n:
                        continue

                    # If either position is blocked, no valid path here
                    if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                        continue

                    prev_max = -1
                    # Check all 4 possible previous states from which dp can be reached
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

                    if prev_max < 0:
                        continue

                    if i1 == i2 and j1 == j2:
                        cherries = grid[i1][j1]
                    else:
                        cherries = grid[i1][j1] + grid[i2][j2]

                    dp[i1][i2][j1] = prev_max + cherries

        result = dp[n - 1][n - 1][n - 1]
        return max(result, 0)