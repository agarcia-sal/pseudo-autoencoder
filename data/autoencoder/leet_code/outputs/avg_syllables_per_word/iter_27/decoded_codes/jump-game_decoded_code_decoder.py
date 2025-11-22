from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            sum_index_and_value = i + nums[i]
            if sum_index_and_value > farthest:
                farthest = sum_index_and_value
        return farthest >= len(nums) - 1