class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for amount in range(1, target + 1):
            for num in nums:
                if amount >= num:
                    dp[amount] += dp[amount - num]
        return dp[target]