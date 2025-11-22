def max_subarray_len(nums, k):
    map = {0: -1}
    sum = 0
    max_len = 0
    for i, v in enumerate(nums):
        sum += v
        if sum - k in map:
            max_len = max(max_len, i - map[sum - k])
        if sum not in map:
            map[sum] = i
    return max_len