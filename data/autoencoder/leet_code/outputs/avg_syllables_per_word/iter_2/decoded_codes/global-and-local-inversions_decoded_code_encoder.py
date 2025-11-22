class Solution:
    def isIdealPermutation(self, nums):
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True