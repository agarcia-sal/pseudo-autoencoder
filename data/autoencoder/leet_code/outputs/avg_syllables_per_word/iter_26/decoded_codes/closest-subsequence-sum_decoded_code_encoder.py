from bisect import bisect_left
from math import inf

class Solution:
    def minAbsDifference(self, nums, goal):
        n = len(nums)
        mid = n // 2

        left_sums = [0]
        for num in nums[:mid]:
            new_sums = []
            for s in left_sums:
                new_sums.append(s + num)
            left_sums.extend(new_sums)

        right_sums = [0]
        for num in nums[mid:]:
            new_sums = []
            for s in right_sums:
                new_sums.append(s + num)
            right_sums.extend(new_sums)

        right_sums.sort()
        min_diff = inf

        for left_sum in left_sums:
            target = goal - left_sum
            pos = bisect_left(right_sums, target)

            if pos < len(right_sums):
                candidate_diff = abs(left_sum + right_sums[pos] - goal)
                if candidate_diff < min_diff:
                    min_diff = candidate_diff

            if pos > 0:
                candidate_diff = abs(left_sum + right_sums[pos - 1] - goal)
                if candidate_diff < min_diff:
                    min_diff = candidate_diff

        return min_diff