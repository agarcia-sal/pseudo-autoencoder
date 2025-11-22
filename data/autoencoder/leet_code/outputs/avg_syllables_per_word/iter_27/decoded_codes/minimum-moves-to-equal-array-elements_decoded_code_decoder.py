from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_num = min(nums)
        total_difference = 0
        for num in nums:
            total_difference += num - min_num
        return total_difference