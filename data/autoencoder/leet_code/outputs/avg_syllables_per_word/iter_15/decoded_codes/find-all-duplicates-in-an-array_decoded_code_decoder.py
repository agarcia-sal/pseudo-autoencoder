from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                tmp = nums[index]
                nums[index] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        duplicate_list = []
        for position, value in enumerate(nums):
            if value != position + 1:
                duplicate_list.append(value)
        return duplicate_list