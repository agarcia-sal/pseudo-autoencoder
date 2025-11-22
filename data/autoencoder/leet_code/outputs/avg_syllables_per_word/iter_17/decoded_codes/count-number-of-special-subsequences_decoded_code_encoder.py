class Solution:
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        dp = [0, 0, 0]  # dp[0]: count of subsequences of 0s, dp[1]: count of subsequences 0s and 1s, dp[2]: count of subsequences 0s,1s,2s

        for number in nums:
            if number == 0:
                dp[0] = (2 * dp[0] + 1) % MOD
            elif number == 1:
                dp[1] = (2 * dp[1] + dp[0]) % MOD
            elif number == 2:
                dp[2] = (2 * dp[2] + dp[1]) % MOD

        return dp[2]