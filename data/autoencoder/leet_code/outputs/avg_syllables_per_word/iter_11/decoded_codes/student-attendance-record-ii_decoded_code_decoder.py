class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = self.initialize_dp(n)
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD
                    if k < 2:
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result

    def initialize_dp(self, n: int):
        dp = []
        for _ in range(n + 1):
            list_j = []
            for _ in range(2):
                list_k = [0, 0, 0]
                list_j.append(list_k)
            dp.append(list_j)
        return dp