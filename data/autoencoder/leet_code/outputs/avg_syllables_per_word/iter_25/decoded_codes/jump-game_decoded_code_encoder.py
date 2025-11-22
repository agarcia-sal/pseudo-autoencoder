from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            candidate = i + nums[i]
            if candidate > farthest:
                farthest = candidate
        return farthest >= len(nums) - 1