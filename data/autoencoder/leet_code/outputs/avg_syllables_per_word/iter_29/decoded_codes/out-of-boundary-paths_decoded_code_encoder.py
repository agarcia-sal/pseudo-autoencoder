class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MODULO_VALUE = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        for moves in range(1, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            dp[row][col][moves] = (dp[row][col][moves] + 1) % MODULO_VALUE
                        else:
                            dp[row][col][moves] = (dp[row][col][moves] + dp[nr][nc][moves - 1]) % MODULO_VALUE

        return dp[startRow][startColumn][maxMove]