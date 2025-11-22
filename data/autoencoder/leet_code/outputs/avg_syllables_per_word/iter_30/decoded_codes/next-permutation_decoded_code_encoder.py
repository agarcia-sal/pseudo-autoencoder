from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        start_position, end_position = i + 1, len(nums) - 1
        while start_position < end_position:
            nums[start_position], nums[end_position] = nums[end_position], nums[start_position]
            start_position += 1
            end_position -= 1