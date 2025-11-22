class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = self.constructor_dp(n, numCarpets)

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + self.check_tile_at_position(i - 1, floor)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                option_without_carpet = dp[i - 1][j] + self.check_tile_at_position(i - 1, floor)
                option_with_carpet = dp[max(0, i - carpetLen)][j - 1]
                dp[i][j] = min(option_without_carpet, option_with_carpet)

        return dp[n][numCarpets]

    def constructor_dp(self, n: int, numCarpets: int) -> list:
        return [[0] * (numCarpets + 1) for _ in range(n + 1)]

    def check_tile_at_position(self, index: int, floor: str) -> int:
        return 1 if floor[index] == '1' else 0