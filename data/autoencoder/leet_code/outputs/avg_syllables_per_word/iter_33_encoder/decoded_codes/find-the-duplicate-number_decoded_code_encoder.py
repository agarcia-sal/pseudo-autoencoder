class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count = 0
            for v in nums:
                if v <= x:
                    count += 1
            return count > x

        left_boundary = 0
        right_boundary = len(nums) - 1
        while left_boundary < right_boundary:
            middle_point = left_boundary + (right_boundary - left_boundary) // 2
            if f(middle_point):
                right_boundary = middle_point
            else:
                left_boundary = middle_point + 1
        return left_boundary