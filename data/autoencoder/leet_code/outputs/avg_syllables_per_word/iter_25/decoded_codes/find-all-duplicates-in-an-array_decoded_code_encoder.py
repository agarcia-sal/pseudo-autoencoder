from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        result_list = []
        for i, v in enumerate(nums):
            if v != i + 1:
                result_list.append(v)
        return result_list