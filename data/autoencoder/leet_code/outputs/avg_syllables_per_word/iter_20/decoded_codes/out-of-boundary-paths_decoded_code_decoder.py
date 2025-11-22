class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dp = self.initialize_dp_array(m, n, maxMove + 1)

        for move in range(1, maxMove + 1):
            for r in range(m):
                for c in range(n):
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            dp[r][c][move] = (dp[r][c][move] + 1) % MOD
                        else:
                            dp[r][c][move] = (dp[r][c][move] + dp[nr][nc][move - 1]) % MOD

        return dp[startRow][startColumn][maxMove]

    def initialize_dp_array(self, rows: int, columns: int, depth: int):
        return [[[0] * depth for _ in range(columns)] for __ in range(rows)]