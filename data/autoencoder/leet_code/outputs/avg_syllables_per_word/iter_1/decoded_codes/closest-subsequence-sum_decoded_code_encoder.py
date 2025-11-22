from bisect import bisect_left

def min_abs_diff(nums, goal):
    n = len(nums)
    mid = n // 2

    left_sums = [0]
    for num in nums[:mid]:
        left_sums += [s + num for s in left_sums]

    right_sums = [0]
    for num in nums[mid:]:
        right_sums += [s + num for s in right_sums]

    right_sums.sort()

    min_diff = float('inf')
    for ls in left_sums:
        target = goal - ls
        pos = bisect_left(right_sums, target)
        if pos < len(right_sums):
            min_diff = min(min_diff, abs(ls + right_sums[pos] - goal))
        if pos > 0:
            min_diff = min(min_diff, abs(ls + right_sums[pos-1] - goal))

    return min_diff