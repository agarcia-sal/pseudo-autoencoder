from typing import List, Dict
from itertools import combinations
import math

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum / 2
        min_diff = math.inf

        left_half = nums[:n]
        right_half = nums[n:]

        # left_sums[i] and right_sums[i] are dicts mapping subset sums of subsets of size i to their frequency
        left_sums: List[Dict[int, int]] = [{} for _ in range(n + 1)]
        right_sums: List[Dict[int, int]] = [{} for _ in range(n + 1)]

        for i in range(n + 1):
            # For left half
            for comb in combinations(left_half, i):
                subset_sum = sum(comb)
                left_sums[i][subset_sum] = left_sums[i].get(subset_sum, 0) + 1
            # For right half
            for comb in combinations(right_half, i):
                subset_sum = sum(comb)
                right_sums[i][subset_sum] = right_sums[i].get(subset_sum, 0) + 1

        for i in range(n + 1):
            left_values = sorted(left_sums[i].keys())
            right_values = sorted(right_sums[n - i].keys())

            j = 0
            k = len(right_values) - 1

            # Two-pointer approach to find sums closest to target
            while j < len(left_values) and k >= 0:
                current_sum = left_values[j] + right_values[k]
                current_diff = abs(total_sum - 2 * current_sum)

                if current_diff < min_diff:
                    min_diff = current_diff

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    # Exact half sum found, difference is zero
                    return 0

        return min_diff