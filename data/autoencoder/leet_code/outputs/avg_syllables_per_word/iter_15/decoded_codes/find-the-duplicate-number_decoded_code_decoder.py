from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count_of_elements_less_than_or_equal_to_x = 0
            for v in nums:
                if v <= x:
                    count_of_elements_less_than_or_equal_to_x += 1
            return count_of_elements_less_than_or_equal_to_x > x

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left