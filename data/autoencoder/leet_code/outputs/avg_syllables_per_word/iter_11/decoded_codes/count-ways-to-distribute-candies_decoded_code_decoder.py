class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = self.initialize_dp_array(n + 1, k + 1)
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                product = j * dp[i - 1][j]
                total = product + dp[i - 1][j - 1]
                dp[i][j] = total % MOD
        return dp[n][k]

    def initialize_dp_array(self, n_length: int, k_length: int) -> list:
        return [[0] * k_length for _ in range(n_length)]