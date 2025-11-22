class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MODULO_CONSTANT = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Initialize 3D DP list: dp[row][column][step]
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        for step in range(1, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    for dr, dc in directions:
                        newRow, newCol = row + dr, col + dc
                        if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                            dp[row][col][step] = (dp[row][col][step] + 1) % MODULO_CONSTANT
                        else:
                            dp[row][col][step] = (dp[row][col][step] + dp[newRow][newCol][step - 1]) % MODULO_CONSTANT

        return dp[startRow][startColumn][maxMove]