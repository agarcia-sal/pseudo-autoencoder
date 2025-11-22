from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total_slices = 0
        current_length = 2

        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                current_length += 1
                total_slices += current_length - 2
            else:
                current_length = 2

        return total_slices