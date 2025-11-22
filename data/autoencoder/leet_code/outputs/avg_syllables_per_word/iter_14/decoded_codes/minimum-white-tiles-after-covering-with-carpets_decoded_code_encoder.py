class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = self.initialize_dp_array(n, numCarpets)

        for i in range(1, n + 1):
            previous_dp_value = dp[i - 1][0]
            is_current_tile_white = 1 if floor[i - 1] == '1' else 0
            dp[i][0] = previous_dp_value + is_current_tile_white

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                is_current_tile_white = 1 if floor[i - 1] == '1' else 0
                dp_value_without_carpet = dp[i - 1][j] + is_current_tile_white
                starting_index = max(0, i - carpetLen)
                dp_value_with_carpet = dp[starting_index][j - 1]
                dp[i][j] = min(dp_value_without_carpet, dp_value_with_carpet)

        return dp[n][numCarpets]

    def initialize_dp_array(self, n: int, numCarpets: int) -> list:
        return [[0] * (numCarpets + 1) for _ in range(n + 1)]