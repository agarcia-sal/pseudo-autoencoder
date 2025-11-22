from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            count = 0
            for value in nums:
                if value <= x:
                    count += 1
            return count > x

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left