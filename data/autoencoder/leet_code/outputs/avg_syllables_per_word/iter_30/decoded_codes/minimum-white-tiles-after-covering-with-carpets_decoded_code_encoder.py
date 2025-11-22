class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j]: minimum white tiles left after covering first i tiles using j carpets
        # However, according to the pseudocode, dp stores count of white tiles uncovered up to i with j carpets used
        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        # Initialize dp for 0 carpets
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if floor[i - 1] == '1' else 0)

        for j in range(1, numCarpets + 1):
            for i in range(1, n + 1):
                # Count white tiles if we do not put carpet ending at i
                dp[i][j] = dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0)
                # Check if placing a carpet covering carpetLen tiles ending at i reduces white tiles
                start = max(0, i - carpetLen)
                if dp[i][j] > dp[start][j - 1]:
                    dp[i][j] = dp[start][j - 1]

        return dp[n][numCarpets]