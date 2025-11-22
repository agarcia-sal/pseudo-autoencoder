class Solution:
    def numTilings(self, n: int) -> int:
        MODULO = 10**9 + 7
        dp = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
        if n >= 2:
            dp[2] = 2
            dp1[2] = 1
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp1[i - 1]) % MODULO
            dp1[i] = (dp[i - 2] + dp1[i - 1]) % MODULO
        return dp[n]