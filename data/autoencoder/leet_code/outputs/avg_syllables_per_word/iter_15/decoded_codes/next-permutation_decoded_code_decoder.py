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
        self.reverseSubsequence(nums, i + 1, len(nums) - 1)

    def reverseSubsequence(self, nums: List[int], start_position: int, end_position: int) -> None:
        left_pointer = start_position
        right_pointer = end_position
        while left_pointer < right_pointer:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer -= 1