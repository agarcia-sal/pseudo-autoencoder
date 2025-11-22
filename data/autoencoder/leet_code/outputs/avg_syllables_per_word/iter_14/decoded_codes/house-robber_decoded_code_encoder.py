class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]

        if nums[0] >= nums[1]:
            dp[1] = nums[0]
        else:
            dp[1] = nums[1]

        for i in range(2, len(nums)):
            if dp[i - 1] >= dp[i - 2] + nums[i]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 2] + nums[i]

        return dp[-1]