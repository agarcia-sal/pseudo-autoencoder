from typing import List
import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second = -math.inf
        stack = []
        # Traverse from right to left
        for num in reversed(nums):
            # If we find a number less than 'second', pattern found
            if num < second:
                return True
            while stack and stack[-1] < num:
                second = stack.pop()
            stack.append(num)
        return False