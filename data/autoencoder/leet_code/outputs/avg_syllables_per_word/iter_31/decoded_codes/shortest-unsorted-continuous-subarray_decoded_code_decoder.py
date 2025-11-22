from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        start = -1
        end = -2  # end < start to handle already sorted case
        for index in range(len(nums)):
            if nums[index] != sorted_list[index]:
                if start == -1:
                    start = index
                end = index
        return end - start + 1