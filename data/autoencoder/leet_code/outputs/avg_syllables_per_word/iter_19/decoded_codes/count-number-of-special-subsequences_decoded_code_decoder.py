class Solution:
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        dp = [0, 0, 0]  # counts of subsequences ending with 0, 1, and 2
        for num in nums:
            if num == 0:
                dp[0] = (2 * dp[0] + 1) % MOD
            elif num == 1:
                dp[1] = (2 * dp[1] + dp[0]) % MOD
            elif num == 2:
                dp[2] = (2 * dp[2] + dp[1]) % MOD
        return dp[2]