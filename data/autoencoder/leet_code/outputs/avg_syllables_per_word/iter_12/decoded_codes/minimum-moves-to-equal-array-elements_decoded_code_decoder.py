class Solution:
    def minMoves(self, nums):
        min_num = min(nums)
        total = 0
        for num in nums:
            total += num - min_num
        return total