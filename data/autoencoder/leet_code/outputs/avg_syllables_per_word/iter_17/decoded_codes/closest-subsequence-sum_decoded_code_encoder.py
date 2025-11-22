from bisect import bisect_left
from math import inf

class Solution:
    def minAbsDifference(self, nums, goal):
        n = len(nums)
        mid = n // 2

        left_sums = [0]
        for number in nums[:mid]:
            new_sums = [sum_value + number for sum_value in left_sums]
            left_sums.extend(new_sums)

        right_sums = [0]
        for number in nums[mid:]:
            new_sums = [sum_value + number for sum_value in right_sums]
            right_sums.extend(new_sums)

        right_sums.sort()

        min_diff = inf

        for left_sum in left_sums:
            target = goal - left_sum
            pos = bisect_left(right_sums, target)

            if pos < len(right_sums):
                min_diff = min(min_diff, abs(left_sum + right_sums[pos] - goal))
            if pos > 0:
                min_diff = min(min_diff, abs(left_sum + right_sums[pos - 1] - goal))

        return min_diff