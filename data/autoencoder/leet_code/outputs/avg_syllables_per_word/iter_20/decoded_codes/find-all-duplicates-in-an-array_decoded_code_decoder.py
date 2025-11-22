from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                temp = nums[index]
                nums[index], nums[temp - 1] = nums[temp - 1], temp
        result_list = []
        for i, val in enumerate(nums):
            if val != i + 1:
                result_list.append(val)
        return result_list