from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            return sum(value <= x for value in nums) > x
        return bisect_left(range(len(nums)), True, key=f)