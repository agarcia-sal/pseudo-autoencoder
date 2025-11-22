class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = self.initialize_dp(n + 1, numCarpets + 1)

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (floor[i - 1] == '1')

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + (floor[i - 1] == '1')
                dp[i][j] = min(dp[i][j], dp[max(0, i - carpetLen)][j - 1])

        return dp[n][numCarpets]

    def initialize_dp(self, rows: int, cols: int) -> list[list[int]]:
        result = []
        for _ in range(rows):
            row = [0] * cols
            result.append(row)
        return result