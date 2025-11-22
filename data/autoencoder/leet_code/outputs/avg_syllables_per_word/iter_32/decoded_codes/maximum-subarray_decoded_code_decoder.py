from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            # If the input list is empty, return 0 (or could raise an error depending on context)
            return 0

        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = num if num > current_sum + num else current_sum + num
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum