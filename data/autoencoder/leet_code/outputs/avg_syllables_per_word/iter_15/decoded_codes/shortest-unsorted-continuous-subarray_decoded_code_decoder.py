from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = -1
        end = -2
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start == -1:
                    start = i
                end = i
        result_length = end - start + 1
        return result_length