from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for number in nums:
            while stack:
                g = gcd(stack[-1], number)
                if g == 1:
                    break
                number = stack.pop() * number // g
            stack.append(number)
        return stack