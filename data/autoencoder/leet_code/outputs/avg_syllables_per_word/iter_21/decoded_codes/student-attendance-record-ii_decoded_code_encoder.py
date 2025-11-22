class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = self.initialize_dp(n)
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    self.add_present(dp, i, j, k, MOD)
                    if j == 0:
                        self.add_absent(dp, i, k, MOD)
                    if k < 2:
                        self.add_late(dp, i, j, k, MOD)

        result = 0
        for j in range(2):
            for k in range(3):
                result += dp[n][j][k]
        return result % MOD

    def initialize_dp(self, n: int):
        # dp[i][j][k]: number of sequences of length i with j absents and k continuous lates
        return [[[0]*3 for _ in range(2)] for _ in range(n+1)]

    def add_present(self, dp, i, j, k, MOD):
        dp[i][j][0] += dp[i - 1][j][k]
        dp[i][j][0] %= MOD

    def add_absent(self, dp, i, k, MOD):
        dp[i][1][0] += dp[i - 1][0][k]
        dp[i][1][0] %= MOD

    def add_late(self, dp, i, j, k, MOD):
        dp[i][j][k + 1] += dp[i - 1][j][k]
        dp[i][j][k + 1] %= MOD