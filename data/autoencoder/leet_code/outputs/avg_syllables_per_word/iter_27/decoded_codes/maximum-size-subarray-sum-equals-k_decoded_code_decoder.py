from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cumulative_sum_index = {0: -1}
        cumulative_sum = 0
        max_length = 0

        for index, num in enumerate(nums):
            cumulative_sum += num
            if (cumulative_sum - k) in cumulative_sum_index:
                max_length = max(max_length, index - cumulative_sum_index[cumulative_sum - k])
            if cumulative_sum not in cumulative_sum_index:
                cumulative_sum_index[cumulative_sum] = index

        return max_length