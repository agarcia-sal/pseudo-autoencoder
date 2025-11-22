from typing import List, Tuple

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            dp[i][j][k] = (dp[i][j][k] + 1) % MOD
                        else:
                            dp[i][j][k] = (dp[i][j][k] + dp[ni][nj][k - 1]) % MOD

        return dp[startRow][startColumn][maxMove]