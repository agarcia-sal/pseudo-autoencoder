class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count_of_values_less_than_or_equal_to_x = 0
            for value in nums:
                if value <= x:
                    count_of_values_less_than_or_equal_to_x += 1
            return count_of_values_less_than_or_equal_to_x > x

        left_boundary = 0
        right_boundary = len(nums) - 1
        while left_boundary < right_boundary:
            middle_point = left_boundary + (right_boundary - left_boundary) // 2
            if f(middle_point):
                right_boundary = middle_point
            else:
                left_boundary = middle_point + 1
        return left_boundary