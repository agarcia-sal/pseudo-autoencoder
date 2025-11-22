from bisect import bisect_right

class Solution:
    def findDuplicate(self, nums):
        # Helper function returns True if count of elements <= x > x
        def f(x):
            # Count elements <= x using bisect_right on sorted nums
            count = bisect_right(sorted_nums, x)
            return count > x

        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1  # right bound is len(nums) - 1 because nums contains n+1 elements in range [1,n]

        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left