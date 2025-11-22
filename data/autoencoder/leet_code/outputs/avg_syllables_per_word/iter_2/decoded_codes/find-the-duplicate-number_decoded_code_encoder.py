from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count = 0
            for value in nums:
                if value <= x:
                    count += 1
            return count > x

        return bisect_left(range(len(nums)), True, key=f)