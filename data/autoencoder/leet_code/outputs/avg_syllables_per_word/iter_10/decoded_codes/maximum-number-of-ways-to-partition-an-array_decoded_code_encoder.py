from collections import defaultdict

class Solution:
    def waysToPartition(self, nums, k):
        total_sum = sum(nums)
        n = len(nums)

        left_diff = defaultdict(int)
        right_diff = defaultdict(int)

        current_sum = 0
        for i in range(n - 1):
            current_sum += nums[i]
            diff = total_sum - 2 * current_sum
            right_diff[diff] += 1

        max_ways = right_diff.get(0, 0)

        current_sum = 0
        for i in range(n):
            current_sum += nums[i]

            diff_change = k - nums[i]
            new_ways = left_diff[-diff_change] + right_diff.get(diff_change, 0)
            if new_ways > max_ways:
                max_ways = new_ways

            diff = total_sum - 2 * current_sum
            right_diff[diff] -= 1
            left_diff[diff] += 1

        return max_ways