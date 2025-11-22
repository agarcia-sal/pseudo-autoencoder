from bisect import bisect_right

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            # Count how many numbers in nums are less than or equal to x
            return sum(v <= x for v in nums)
        n = len(nums)
        # Binary search for the smallest x in [0, n) where f(x) > x
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if f(mid) > mid:
                right = mid
            else:
                left = mid + 1
        return left