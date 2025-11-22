class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            prefix_sum = 0
            for j in range(k + 1):
                prefix_sum += dp[i - 1][j]
                if prefix_sum >= MOD:
                    prefix_sum -= MOD
                if j >= i:
                    prefix_sum -= dp[i - 1][j - i]
                    prefix_sum += MOD
                    if prefix_sum >= MOD:
                        prefix_sum -= MOD
                dp[i][j] = prefix_sum

        return dp[n][k]