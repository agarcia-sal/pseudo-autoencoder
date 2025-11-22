from typing import List

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # dp[k][i][j] = number of paths to move out of boundary starting from (i, j) with exactly k moves
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    count = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            count += 1
                        else:
                            count += dp[k - 1][ni][nj]
                    dp[k][i][j] = count % MOD

        return dp[maxMove][startRow][startColumn]