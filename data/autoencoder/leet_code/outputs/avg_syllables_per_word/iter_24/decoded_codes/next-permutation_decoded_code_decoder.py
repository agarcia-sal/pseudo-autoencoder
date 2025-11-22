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

        self.reverseSublist(nums, i + 1, len(nums) - 1)

    def reverseSublist(self, nums: List[int], start_index: int, end_index: int) -> None:
        while start_index < end_index:
            nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
            start_index += 1
            end_index -= 1