from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            possible_reach = i + nums[i]
            if possible_reach > farthest:
                farthest = possible_reach
        return farthest >= len(nums) - 1