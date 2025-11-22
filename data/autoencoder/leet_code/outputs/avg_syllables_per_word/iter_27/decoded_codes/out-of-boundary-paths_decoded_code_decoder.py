from typing import List

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # dp[i][j][k] = number of ways to move out of boundary starting from cell (i, j) with k moves remaining
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for __ in range(m)]

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    count = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            count += 1
                        else:
                            count += dp[ni][nj][k - 1]
                    dp[i][j][k] = count % MOD

        return dp[startRow][startColumn][maxMove]