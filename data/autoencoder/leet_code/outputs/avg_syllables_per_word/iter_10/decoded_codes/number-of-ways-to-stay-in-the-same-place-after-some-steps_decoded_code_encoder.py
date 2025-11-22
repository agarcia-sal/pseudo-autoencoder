class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MODULO = 10**9 + 7
        max_index = min(steps // 2, arrLen - 1)
        dp = [0] * (max_index + 1)
        dp[0] = 1

        for _ in range(steps):
            prev_dp = dp[:]
            for i in range(max_index + 1):
                dp[i] = prev_dp[i]
                if i > 0:
                    dp[i] = (dp[i] + prev_dp[i - 1]) % MODULO
                if i < max_index:
                    dp[i] = (dp[i] + prev_dp[i + 1]) % MODULO
        return dp[0]