class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        def initialize_three_dimensional_list(length, limit_one, limit_two):
            result = []
            for _ in range(length + 1):
                layer = []
                for _ in range(limit_one):
                    layer.append([0] * limit_two)
                result.append(layer)
            return result

        dp = initialize_three_dimensional_list(n, 2, 3)
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