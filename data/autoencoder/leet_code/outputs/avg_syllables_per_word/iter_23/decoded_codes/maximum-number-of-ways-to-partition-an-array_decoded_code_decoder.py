from collections import defaultdict
from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        n = len(nums)
        left_diff = defaultdict(int)
        right_diff = defaultdict(int)

        current_sum = 0
        # Initialize right_diff with differences for partitions before each index except last
        for i in range(n - 1):
            current_sum += nums[i]
            diff = total_sum - 2 * current_sum
            right_diff[diff] += 1

        max_ways = right_diff[0]
        current_sum = 0

        for i in range(n):
            current_sum += nums[i]
            diff_change = k - nums[i]
            new_ways = left_diff[-diff_change] + right_diff[diff_change]
            if new_ways > max_ways:
                max_ways = new_ways

            diff = total_sum - 2 * current_sum
            # Move this partition diff from right_diff to left_diff
            right_diff[diff] -= 1
            if right_diff[diff] == 0:
                del right_diff[diff]
            left_diff[diff] += 1

        return max_ways