class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k]: number of sequences of length i,
        # with j 'A's used (0 or 1),
        # and k consecutive 'L's at the end (0 to 2).
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Add 'P' (present), resets consecutive L's to 0, j remains same
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                    # Add 'A' (absent), only if we haven't used 'A' yet (j == 0)
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][j][k]) % MOD

                    # Add 'L' (late), only if consecutive L's < 2
                    if k < 2:
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result