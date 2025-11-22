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
                left_choice = mul * nums[left] + dp[left + 1]
                right_choice = mul * nums[right] + dp[left]
                new_dp[left] = left_choice if left_choice > right_choice else right_choice
            dp = new_dp
        return dp[0]