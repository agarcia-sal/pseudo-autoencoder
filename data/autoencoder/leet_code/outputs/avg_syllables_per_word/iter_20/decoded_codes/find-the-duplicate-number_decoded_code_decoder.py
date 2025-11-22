from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            # Count how many numbers are <= x and check if count > x
            count = 0
            # Since nums can be large, use sum with generator expression for efficiency
            count = sum(1 for v in nums if v <= x)
            return count > x

        # Binary search for the smallest x in [0, len(nums)) where f(x) is True
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left