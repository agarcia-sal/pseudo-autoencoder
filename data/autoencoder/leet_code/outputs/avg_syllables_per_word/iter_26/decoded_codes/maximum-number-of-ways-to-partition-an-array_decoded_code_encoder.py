from collections import defaultdict
from typing import List

class Solution:
    def waysToPartition(self, list_nums: List[int], single_value_k: int) -> int:
        total_sum = sum(list_nums)
        n = len(list_nums)

        left_diff = defaultdict(int)
        right_diff = defaultdict(int)

        current_sum = 0
        # Initialize right_diff with all prefix sums except the last index
        for i in range(n - 1):
            current_sum += list_nums[i]
            diff = total_sum - 2 * current_sum
            right_diff[diff] += 1

        max_ways = right_diff[0]

        current_sum = 0
        for i in range(n):
            current_sum += list_nums[i]

            diff_change = single_value_k - list_nums[i]

            new_ways = left_diff[-diff_change] + right_diff[diff_change]

            if new_ways > max_ways:
                max_ways = new_ways

            diff = total_sum - 2 * current_sum
            right_diff[diff] -= 1
            left_diff[diff] += 1

        return max_ways