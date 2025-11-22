class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        # Initialize dp for zero carpets used
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # Without using a carpet at i-th tile
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                # Using a carpet covering up to carpetLen tiles ending at i-th tile
                dp[i][j] = min(dp[i][j], dp[max(0, i - carpetLen)][j - 1])

        return dp[n][numCarpets]