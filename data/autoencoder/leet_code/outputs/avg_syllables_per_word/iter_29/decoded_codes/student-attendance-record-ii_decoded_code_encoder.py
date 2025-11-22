class Solution:
    def checkRecord(self, n: int) -> int:
        MODULO_VALUE = 10**9 + 7

        # dp[i][j][k]: number of valid sequences of length i,
        # with j absents ('A') used (0 or 1),
        # and k continuous lates ('L') count (0 to 2)
        dp = [[[0] * 3 for _ in range(2)] for __ in range(n + 1)]

        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Append 'P': resets late count to 0
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MODULO_VALUE

                    # Append 'A': can only append if no 'A' used yet (j == 0),
                    # increments absents count to 1, resets late count to 0
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i-1][j][k]) % MODULO_VALUE

                    # Append 'L': can only append if k < 2,
                    # increments late count by 1, absents count stays the same
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MODULO_VALUE

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MODULO_VALUE

        return result