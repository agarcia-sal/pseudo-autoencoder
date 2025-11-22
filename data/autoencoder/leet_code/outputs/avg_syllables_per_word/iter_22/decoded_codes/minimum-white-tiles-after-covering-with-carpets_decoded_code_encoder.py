class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        # Initialize dp for zero carpets
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (floor[i - 1] == '1')

        # Fill dp for using carpets from 1 to numCarpets
        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # Without placing a new carpet at position i
                dp[i][j] = dp[i - 1][j] + (floor[i - 1] == '1')
                # Place a carpet covering carpetLen tiles ending at position i
                prev_index = max(0, i - carpetLen)
                dp[i][j] = min(dp[i][j], dp[prev_index][j - 1])

        return dp[n][numCarpets]