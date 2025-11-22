from bisect import bisect_left, bisect_right, insort

def count_range_sum(nums, lower, upper):
    prefix_sums = [0]
    curr_sum = 0
    count = 0
    for num in nums:
        curr_sum += num
        left = curr_sum - upper
        right = curr_sum - lower
        count += bisect_right(prefix_sums, right) - bisect_left(prefix_sums, left)
        insort(prefix_sums, curr_sum)
    return count