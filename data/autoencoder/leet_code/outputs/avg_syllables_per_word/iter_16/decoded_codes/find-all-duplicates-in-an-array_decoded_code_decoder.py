from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                tmp = nums[index]
                nums[index] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        result_list = []
        for index, value in enumerate(nums):
            if value != index + 1:
                result_list.append(value)
        return result_list