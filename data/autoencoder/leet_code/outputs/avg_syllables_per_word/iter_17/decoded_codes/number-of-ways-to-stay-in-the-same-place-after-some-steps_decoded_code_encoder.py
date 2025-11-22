class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MODULUS = 10**9 + 7
        maximum_index = min(steps // 2, arrLen - 1)
        dp = [0] * (maximum_index + 1)
        dp[0] = 1

        for _ in range(1, steps + 1):
            previous_dp = dp[:]
            for index in range(maximum_index + 1):
                dp[index] = previous_dp[index]
                if index > 0:
                    dp[index] = (dp[index] + previous_dp[index - 1]) % MODULUS
                if index < maximum_index:
                    dp[index] = (dp[index] + previous_dp[index + 1]) % MODULUS

        return dp[0]