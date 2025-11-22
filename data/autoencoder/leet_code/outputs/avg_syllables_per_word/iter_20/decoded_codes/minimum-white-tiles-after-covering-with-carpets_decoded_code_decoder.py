class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = self.initialize_two_dimensional_list(n + 1, numCarpets + 1)

        # Convert floor characters to integer list for faster access: '1'->1, else 0
        floor_int = [1 if c == '1' else 0 for c in floor]

        # dp[i][0]: minimum white tiles for first i tiles using 0 carpets
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + floor_int[i - 1]

        # Fill dp for 1 to numCarpets
        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # Not placing a carpet on current tile
                cost_without_carpet = dp[i - 1][j] + floor_int[i - 1]

                # Placing a carpet covering carpetLen tiles ending at current position i
                # start idx is max(0, i - carpetLen)
                start = max(0, i - carpetLen)
                cost_with_carpet = dp[start][j - 1]

                dp[i][j] = min(cost_without_carpet, cost_with_carpet)

        return dp[n][numCarpets]

    def initialize_two_dimensional_list(self, rows: int, columns: int) -> list[list[int]]:
        return [[0] * columns for _ in range(rows)]