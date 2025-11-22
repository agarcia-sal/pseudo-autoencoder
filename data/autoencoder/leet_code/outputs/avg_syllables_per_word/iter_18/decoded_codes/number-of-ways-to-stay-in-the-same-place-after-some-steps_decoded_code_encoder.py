class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_index = min(steps // 2, arrLen - 1)
        dp = [0] * (max_index + 1)
        dp[0] = 1
        for _ in range(1, steps + 1):
            prev_dp = dp[:]
            for pos in range(max_index + 1):
                dp[pos] = prev_dp[pos]
                if pos > 0:
                    dp[pos] = (dp[pos] + prev_dp[pos - 1]) % MOD
                if pos < max_index:
                    dp[pos] = (dp[pos] + prev_dp[pos + 1]) % MOD
        return dp[0]