from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Update 'ones' with current num bits not in 'twos'
            ones = (ones ^ num) & ~twos
            # Update 'twos' with current num bits not in updated 'ones'
            twos = (twos ^ num) & ~ones
        return ones