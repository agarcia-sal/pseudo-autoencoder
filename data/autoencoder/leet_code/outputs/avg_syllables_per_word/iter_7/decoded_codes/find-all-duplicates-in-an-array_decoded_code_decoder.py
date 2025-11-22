from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        result = []
        for index, value in enumerate(nums):
            if value != index + 1:
                result.append(value)
        return result