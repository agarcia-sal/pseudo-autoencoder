from math import inf
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second = -inf
        stack = []
        for num in reversed(nums):
            if num < second:
                return True
            while stack and stack[-1] < num:
                second = stack.pop()
            stack.append(num)
        return False