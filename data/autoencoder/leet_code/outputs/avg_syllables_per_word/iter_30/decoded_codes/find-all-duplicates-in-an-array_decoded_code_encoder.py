from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # Swap until the element at i is at the correct position or a duplicate is found
            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        result_list = []
        for i, v in enumerate(nums):
            if v != i + 1:
                result_list.append(v)
        return result_list