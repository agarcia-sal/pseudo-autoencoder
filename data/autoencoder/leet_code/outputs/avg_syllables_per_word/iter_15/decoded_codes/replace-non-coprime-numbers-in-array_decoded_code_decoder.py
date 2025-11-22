from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for number in nums:
            while stack:
                greatest_common_divisor = gcd(stack[-1], number)
                if greatest_common_divisor == 1:
                    break
                number = stack.pop() * number // greatest_common_divisor
            stack.append(number)
        return stack