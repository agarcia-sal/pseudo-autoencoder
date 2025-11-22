class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 3 for _ in range(2)] for __ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Adding 'P' (present) resets consecutive 'L' count to 0
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                    if j == 0:
                        # Adding 'A' (absent) only if no 'A' used before
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

                    if k < 2:
                        # Adding 'L' (late) increases consecutive 'L' count by 1
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result