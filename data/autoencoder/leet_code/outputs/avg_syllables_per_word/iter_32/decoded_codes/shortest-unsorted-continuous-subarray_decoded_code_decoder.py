from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start, end = -1, -2  # initialize so that if already sorted, end - start + 1 = 0
        for index in range(len(nums)):
            if nums[index] != sorted_nums[index]:
                if start == -1:
                    start = index
                end = index
        return end - start + 1