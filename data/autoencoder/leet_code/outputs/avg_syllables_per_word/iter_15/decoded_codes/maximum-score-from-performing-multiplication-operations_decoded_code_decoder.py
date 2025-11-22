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
                score_if_left_chosen = mul * nums[left] + dp[left + 1]
                score_if_right_chosen = mul * nums[right] + dp[left]
                new_dp[left] = max(score_if_left_chosen, score_if_right_chosen)
            dp = new_dp
        return dp[0]