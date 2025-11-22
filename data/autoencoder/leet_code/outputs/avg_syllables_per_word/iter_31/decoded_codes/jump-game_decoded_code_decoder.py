from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n):
            if i > farthest:
                return False
            max_candidate = i + nums[i]
            if max_candidate > farthest:
                farthest = max_candidate
            if farthest >= n - 1:
                return True
        return False