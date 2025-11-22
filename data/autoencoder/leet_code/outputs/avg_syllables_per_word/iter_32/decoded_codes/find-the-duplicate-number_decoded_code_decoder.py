from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            # Count how many numbers are less than or equal to x
            count_of_values_less_than_or_equal_to_x = sum(1 for value in nums if value <= x)
            return count_of_values_less_than_or_equal_to_x > x

        left, right = 0, len(nums) - 1
        # Binary search for smallest x where f(x) is True
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left