from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count = 0
            for v in nums:
                if v <= x:
                    count += 1
            return count > x

        n = len(nums)
        return bisect_left(range(n), True, key=f)