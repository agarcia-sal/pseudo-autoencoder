from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            current_reach = i + nums[i]
            if current_reach > farthest:
                farthest = current_reach
        return farthest >= len(nums) - 1