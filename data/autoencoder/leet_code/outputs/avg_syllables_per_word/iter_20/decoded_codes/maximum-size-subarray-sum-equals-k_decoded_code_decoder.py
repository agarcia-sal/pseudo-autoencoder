from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cumulative_sum_index = {0: -1}
        cumulative_sum = 0
        max_length = 0

        for index, number in enumerate(nums):
            cumulative_sum += number
            if (cumulative_sum - k) in cumulative_sum_index:
                current_length = index - cumulative_sum_index[cumulative_sum - k]
                if current_length > max_length:
                    max_length = current_length
            if cumulative_sum not in cumulative_sum_index:
                cumulative_sum_index[cumulative_sum] = index

        return max_length