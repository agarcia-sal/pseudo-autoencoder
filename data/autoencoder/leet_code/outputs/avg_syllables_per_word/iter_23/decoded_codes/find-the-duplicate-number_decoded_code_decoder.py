from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            count_of_values_less_than_or_equal_to_x = 0
            for value in nums:
                if value <= x:
                    count_of_values_less_than_or_equal_to_x += 1
            return count_of_values_less_than_or_equal_to_x > x

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left