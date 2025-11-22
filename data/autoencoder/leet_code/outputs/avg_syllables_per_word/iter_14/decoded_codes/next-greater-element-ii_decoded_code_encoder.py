from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n - 1):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                pos = stack.pop()
                result[pos] = nums[index]
            if i < n:
                stack.append(index)

        return result