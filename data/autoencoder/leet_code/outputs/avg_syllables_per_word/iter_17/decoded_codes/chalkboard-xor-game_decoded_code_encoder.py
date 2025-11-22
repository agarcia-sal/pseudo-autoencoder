from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        total_xor_value = 0
        for number in nums:
            total_xor_value ^= number
        if total_xor_value == 0:
            return True
        if len(nums) % 2 == 0:
            return True
        return False