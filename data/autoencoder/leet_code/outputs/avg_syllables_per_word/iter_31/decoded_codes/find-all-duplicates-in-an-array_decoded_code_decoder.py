from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            # Place nums[index] at its correct position until correct or duplicate found
            while nums[index] != nums[nums[index] - 1]:
                tmp = nums[index]
                nums[index], nums[tmp - 1] = nums[tmp - 1], nums[index]
        duplicate_list = []
        for index in range(len(nums)):
            if nums[index] != index + 1:
                duplicate_list.append(nums[index])
        return duplicate_list