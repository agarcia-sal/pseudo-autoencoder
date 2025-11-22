class Solution:
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        dp0, dp1, dp2 = 0, 0, 0
        for num in nums:
            if num == 0:
                dp0 = (2 * dp0 + 1) % MOD
            elif num == 1:
                dp1 = (2 * dp1 + dp0) % MOD
            elif num == 2:
                dp2 = (2 * dp2 + dp1) % MOD
        return dp2