from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            if abs(num - index) > 1:
                return False
        return True