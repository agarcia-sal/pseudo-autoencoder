from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            # Check if count of elements <= x is greater than x
            return sum(1 for v in nums if v <= x) > x

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left