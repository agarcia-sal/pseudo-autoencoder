from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses: List[int]) -> int:
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))