class Solution:
    def minMoves(self, nums):
        min_num = min(nums)
        return sum(num - min_num for num in nums)