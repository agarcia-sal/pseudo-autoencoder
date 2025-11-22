from collections import defaultdict

class Solution:
    def waysToPartition(self, nums, k):
        total_sum = sum(nums)
        n = len(nums)

        left_diff = defaultdict(int)
        right_diff = defaultdict(int)

        current_sum = 0
        for index in range(n):
            current_sum += nums[index]
            diff = total_sum - 2 * current_sum
            right_diff[diff] += 1

        max_ways = right_diff[0]

        current_sum = 0
        for index in range(n):
            current_sum += nums[index]
            diff_change = k - nums[index]
            new_ways = left_diff[-diff_change] + right_diff[diff_change]

            if new_ways > max_ways:
                max_ways = new_ways

            diff = total_sum - 2 * current_sum
            right_diff[diff] -= 1
            left_diff[diff] += 1

        return max_ways