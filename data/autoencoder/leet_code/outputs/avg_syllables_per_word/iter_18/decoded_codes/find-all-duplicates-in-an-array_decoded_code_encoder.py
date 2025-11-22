from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                temp_first = nums[index]
                temp_second = nums[temp_first - 1]
                nums[index] = temp_second
                nums[temp_first - 1] = temp_first
        result_list = []
        for current_index, current_value in enumerate(nums):
            if current_value != current_index + 1:
                result_list.append(current_value)
        return result_list