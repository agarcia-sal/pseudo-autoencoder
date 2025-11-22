from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        if nums[0] > nums[1]:
            dp[1] = nums[0]
        else:
            dp[1] = nums[1]

        for i in range(2, n):
            if dp[i-1] > dp[i-2] + nums[i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2] + nums[i]

        return dp[-1]