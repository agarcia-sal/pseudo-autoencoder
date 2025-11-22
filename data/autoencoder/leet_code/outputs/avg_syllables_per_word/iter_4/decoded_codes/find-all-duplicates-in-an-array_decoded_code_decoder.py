from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result