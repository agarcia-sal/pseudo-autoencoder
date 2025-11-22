from collections import defaultdict
from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        n = len(nums)

        left_diff = defaultdict(int)
        right_diff = defaultdict(int)

        current_sum = 0
        for index in range(n - 1):
            current_sum += nums[index]
            diff = total_sum - 2 * current_sum
            right_diff[diff] += 1

        max_ways = right_diff.get(0, 0)

        current_sum = 0
        for index in range(n):
            current_sum += nums[index]

            diff_change = k - nums[index]

            new_ways = left_diff.get(-diff_change, 0) + right_diff.get(diff_change, 0)
            if new_ways > max_ways:
                max_ways = new_ways

            diff = total_sum - 2 * current_sum
            right_diff[diff] -= 1
            left_diff[diff] += 1

        return max_ways