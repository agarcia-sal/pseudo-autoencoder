from math import inf
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second = -inf
        stack = []
        for number in reversed(nums):
            if number < second:
                return True
            while stack and stack[-1] < number:
                second = stack.pop()
            stack.append(number)
        return False