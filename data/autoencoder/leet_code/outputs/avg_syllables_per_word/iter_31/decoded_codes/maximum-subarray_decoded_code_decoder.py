from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("Input list 'nums' must contain at least one element.")

        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = num if num > current_sum + num else current_sum + num
            if max_sum < current_sum:
                max_sum = current_sum

        return max_sum