from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        length_multipliers = len(multipliers)
        length_nums = len(nums)

        dp = [0] * (length_multipliers + 1)

        for index_i in range(length_multipliers - 1, -1, -1):
            new_dp = [0] * (length_multipliers + 1)
            multiplier_value = multipliers[index_i]
            for left_index in range(index_i + 1):
                right_index = length_nums - 1 - (index_i - left_index)
                left_option = multiplier_value * nums[left_index] + dp[left_index + 1]
                right_option = multiplier_value * nums[right_index] + dp[left_index]
                new_dp[left_index] = max(left_option, right_option)
            dp = new_dp

        return dp[0]