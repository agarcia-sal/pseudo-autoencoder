class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            value_one = dp[i - 1]
            value_two = dp[i - 2] + nums[i]
            dp[i] = max(value_one, value_two)

        return dp[-1]