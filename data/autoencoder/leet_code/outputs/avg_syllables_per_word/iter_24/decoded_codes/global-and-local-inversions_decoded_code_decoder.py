from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for index in range(len(nums)):
            if abs(nums[index] - index) > 1:
                return False
        return True