from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (m + 1)
            mul = multipliers[i]
            for left in range(i + 1):
                right = n - 1 - (i - left)
                score_when_taking_left = mul * nums[left] + dp[left + 1]
                score_when_taking_right = mul * nums[right] + dp[left]
                new_dp[left] = max(score_when_taking_left, score_when_taking_right)
            dp = new_dp
        return dp[0]