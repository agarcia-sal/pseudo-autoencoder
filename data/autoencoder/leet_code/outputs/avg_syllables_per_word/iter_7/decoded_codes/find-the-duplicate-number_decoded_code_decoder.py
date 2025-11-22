from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            count = sum(1 for v in nums if v <= x)
            return count > x

        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left