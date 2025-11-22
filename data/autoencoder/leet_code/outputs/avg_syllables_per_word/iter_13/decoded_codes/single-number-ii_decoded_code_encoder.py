from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Calculate new ones by XOR with num and AND with NOT twos to clear bits present in twos
            ones = (ones ^ num) & ~twos
            # Calculate new twos by XOR with num and AND with NOT updated ones to clear bits present in ones
            twos = (twos ^ num) & ~ones
        return ones