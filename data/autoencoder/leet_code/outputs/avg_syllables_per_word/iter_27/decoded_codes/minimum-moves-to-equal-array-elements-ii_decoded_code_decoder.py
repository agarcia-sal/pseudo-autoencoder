from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        moves = 0
        for num in nums:
            difference = num - median
            if difference < 0:
                absolute_difference = -difference
            else:
                absolute_difference = difference
            moves += absolute_difference
        return moves