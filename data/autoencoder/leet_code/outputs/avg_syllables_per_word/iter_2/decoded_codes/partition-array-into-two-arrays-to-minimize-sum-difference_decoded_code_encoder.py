from itertools import combinations
from collections import defaultdict

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum / 2
        min_diff = float('inf')

        left_half = nums[:n]
        right_half = nums[n:]

        left_sums = [defaultdict(int) for _ in range(n + 1)]
        right_sums = [defaultdict(int) for _ in range(n + 1)]

        for i in range(n + 1):
            for comb in combinations(left_half, i):
                subset_sum = sum(comb)
                left_sums[i][subset_sum] += 1

            for comb in combinations(right_half, i):
                subset_sum = sum(comb)
                right_sums[i][subset_sum] += 1

        for i in range(n + 1):
            left_values = sorted(left_sums[i].keys())
            right_values = sorted(right_sums[n - i].keys())

            j = 0
            k = len(right_values) - 1

            while j < len(left_values) and k >= 0:
                current_sum = left_values[j] + right_values[k]
                diff = abs(total_sum - 2 * current_sum)
                if diff < min_diff:
                    min_diff = diff

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    return 0

        return min_diff