from bisect import bisect_right

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            # Count how many elements in nums are less than or equal to x
            # Using bisect_right after sorting nums for O(log n) queries.
            # To optimize, sort once outside f and reuse.
            return bisect_right(sorted_nums, x) > x

        sorted_nums = sorted(nums)
        low, high = 1, len(nums) - 1  # the duplicate number range based on problem constraints

        while low < high:
            mid = (low + high) // 2
            if f(mid):
                high = mid
            else:
                low = mid + 1

        return low