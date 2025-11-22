class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):  # number of 'A's used
                for k in range(3):  # number of consecutive 'L's at the end
                    # Add 'P': resets consecutive 'L's count to 0
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD

                    # Add 'A': can only add if no 'A' used before (j == 0)
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MOD

                    # Add 'L': can only add if less than 2 consecutive 'L's so far
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        return result