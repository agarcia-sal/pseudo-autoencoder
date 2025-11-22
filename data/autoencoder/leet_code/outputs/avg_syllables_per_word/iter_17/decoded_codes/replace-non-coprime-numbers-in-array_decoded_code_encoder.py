from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, list_of_numbers: List[int]) -> List[int]:
        stack = []
        for number in list_of_numbers:
            while stack:
                greatest_common_divisor = gcd(stack[-1], number)
                if greatest_common_divisor == 1:
                    break
                number = stack.pop() * number // greatest_common_divisor
            stack.append(number)
        return stack