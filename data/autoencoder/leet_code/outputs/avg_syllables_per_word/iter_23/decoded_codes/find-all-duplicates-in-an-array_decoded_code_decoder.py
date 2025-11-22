from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                temp_value = nums[index]
                nums[index] = nums[temp_value - 1]
                nums[temp_value - 1] = temp_value
        result_list = []
        for index, element in enumerate(nums):
            if element != index + 1:
                result_list.append(element)
        return result_list