class Solution:
    def canJump(self, nums):
        farthest = 0
        for index in range(len(nums)):
            if index > farthest:
                return False
            farthest = max(farthest, index + nums[index])
        return farthest >= len(nums) - 1