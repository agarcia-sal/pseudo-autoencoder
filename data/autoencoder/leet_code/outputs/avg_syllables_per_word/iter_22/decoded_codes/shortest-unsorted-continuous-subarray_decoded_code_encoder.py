from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = -1
        end = -2
        for index in range(len(nums)):
            if nums[index] != sorted_nums[index]:
                if start == -1:
                    start = index
                end = index
        return end - start + 1