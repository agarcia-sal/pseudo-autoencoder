from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            return sum(v > x for v in nums)
        n = len(nums) - 1
        pos = bisect_left(range(n + 1), True, key=f)
        return pos