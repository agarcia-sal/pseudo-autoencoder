from typing import List
import bisect
import math

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mid = n // 2

        left_sums = [0]
        for num in nums[:mid]:
            new_sums = [s + num for s in left_sums]
            left_sums.extend(new_sums)

        right_sums = [0]
        for num in nums[mid:]:
            new_sums = [s + num for s in right_sums]
            right_sums.extend(new_sums)

        right_sums.sort()

        min_diff = math.inf
        for left_sum in left_sums:
            target = goal - left_sum
            pos = bisect.bisect_left(right_sums, target)

            if pos < len(right_sums):
                min_diff = min(min_diff, abs(left_sum + right_sums[pos] - goal))
            if pos > 0:
                min_diff = min(min_diff, abs(left_sum + right_sums[pos - 1] - goal))

        return min_diff