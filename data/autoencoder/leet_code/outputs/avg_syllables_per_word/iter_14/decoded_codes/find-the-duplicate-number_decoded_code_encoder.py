from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count = 0
            for value in nums:
                if value <= x:
                    count += 1
            return count > x

        # binary search range: 0..len(nums), find leftmost x with f(x) == True
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left