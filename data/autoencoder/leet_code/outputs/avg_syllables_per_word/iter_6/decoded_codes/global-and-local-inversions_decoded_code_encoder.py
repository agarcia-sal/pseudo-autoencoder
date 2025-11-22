class Solution:
    def isIdealPermutation(self, nums):
        return all(abs(num - i) <= 1 for i, num in enumerate(nums))