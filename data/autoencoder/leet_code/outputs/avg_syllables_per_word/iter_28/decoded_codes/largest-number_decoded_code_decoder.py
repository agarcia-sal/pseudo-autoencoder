from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]

        def compare(x: str, y: str) -> int:
            concatenation_one = x + y
            concatenation_two = y + x
            if concatenation_one > concatenation_two:
                return -1
            elif concatenation_one < concatenation_two:
                return 1
            else:
                return 0

        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0] == '0':
            return '0'
        result = ''.join(nums_str)
        return result