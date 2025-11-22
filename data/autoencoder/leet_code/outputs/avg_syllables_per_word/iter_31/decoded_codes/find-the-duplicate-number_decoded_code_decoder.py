from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count = 0
            for v in nums:
                if v <= x:
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