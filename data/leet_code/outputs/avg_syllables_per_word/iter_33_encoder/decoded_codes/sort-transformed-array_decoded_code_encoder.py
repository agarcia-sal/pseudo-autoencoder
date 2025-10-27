from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x: int) -> int:
            return a * x * x + b * x + c

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        if a >= 0:
            index = n - 1
            while left <= right:
                left_val, right_val = quadratic(nums[left]), quadratic(nums[right])
                if left_val > right_val:
                    result[index] = left_val
                    left += 1
                else:
                    result[index] = right_val
                    right -= 1
                index -= 1
        else:
            index = 0
            while left <= right:
                left_val, right_val = quadratic(nums[left]), quadratic(nums[right])
                if left_val < right_val:
                    result[index] = left_val
                    left += 1
                else:
                    result[index] = right_val
                    right -= 1
                index += 1

        return result