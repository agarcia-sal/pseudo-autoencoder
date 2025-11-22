from collections import defaultdict

def max_ways(nums, k):
    sum_all = sum(nums)
    n = len(nums)
    left_diff = defaultdict(int)
    right_diff = defaultdict(int)
    cur_sum = 0
    for i in range(n-1):
        cur_sum += nums[i]
        diff = sum_all - 2*cur_sum
        right_diff[diff] += 1

    max_ways = right_diff[0]
    cur_sum = 0
    for i in range(n):
        cur_sum += nums[i]
        diff_change = k - nums[i]
        new_ways = left_diff[-diff_change] + right_diff[diff_change]
        max_ways = max(max_ways, new_ways)
        diff = sum_all - 2*cur_sum
        right_diff[diff] -= 1
        left_diff[diff] += 1

    return max_ways