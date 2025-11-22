class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                first_term = dp[i-1][j-1]
                second_term = (i - 1) * dp[i-1][j]
                dp[i][j] = (first_term + second_term) % MOD
        return dp[n][k]