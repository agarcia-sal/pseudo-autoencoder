class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k] represents the count of records of length i,
        # with j 'A's (absence count), and k consecutive 'L's (late count)
        # j in {0,1}, k in {0,1,2}
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1  # base case: empty record

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Add 'P' (present) to all sequences of length i-1 with same absence count j and any late count k
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                    # Add 'A' (absent) if no absence has been taken yet (j == 0)
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

                    # Add 'L' (late) if less than 2 consecutive lates before
                    if k < 2:
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result