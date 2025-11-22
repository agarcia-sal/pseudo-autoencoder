from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)
        dp = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (m + 1)
            mul = multipliers[i]
            for left in range(i + 1):
                right = n - 1 - (i - left)
                value_from_left = mul * nums[left] + dp[left + 1]
                value_from_right = mul * nums[right] + dp[left]
                new_dp[left] = value_from_left if value_from_left > value_from_right else value_from_right
            dp = new_dp
        return dp[0]