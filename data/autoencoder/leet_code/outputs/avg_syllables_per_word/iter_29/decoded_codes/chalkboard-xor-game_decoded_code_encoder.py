from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        if total_xor == 0:
            return True
        if len(nums) % 2 == 0:
            return True
        return False