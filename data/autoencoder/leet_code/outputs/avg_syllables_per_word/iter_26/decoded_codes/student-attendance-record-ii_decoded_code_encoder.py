class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][k] = count of valid sequences of length i with j 'A's used and k trailing 'L's
        dp = [[[0] * 3 for _ in range(2)] for __ in range(n + 1)]

        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # adding 'P' resets trailing L count
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                    if j == 0:
                        # can add 'A' only if no 'A' used before
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

                    if k < 2:
                        # add 'L' only if fewer than 2 trailing Ls
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result