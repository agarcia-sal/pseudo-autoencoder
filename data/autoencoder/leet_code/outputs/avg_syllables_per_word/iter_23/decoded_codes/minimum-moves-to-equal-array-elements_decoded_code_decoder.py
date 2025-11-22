from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        total_difference = 0
        for num in nums:
            difference = num - min_num
            total_difference += difference
        return total_difference