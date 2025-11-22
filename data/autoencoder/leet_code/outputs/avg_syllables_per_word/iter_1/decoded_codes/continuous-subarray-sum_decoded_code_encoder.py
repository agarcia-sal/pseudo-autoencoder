def check_subarray_sum(nums, k):
    remainder_map = {0: -1}
    total_sum = 0
    for i, num in enumerate(nums):
        total_sum += num
        if k != 0:
            total_sum %= k
        if total_sum in remainder_map:
            if i - remainder_map[total_sum] > 1:
                return True
        else:
            remainder_map[total_sum] = i
    return False