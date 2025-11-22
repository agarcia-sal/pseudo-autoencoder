def max_rotate_function(nums):
    n = len(nums)
    if n == 1:
        return 0
    total = sum(nums)
    cur = sum(i * nums[i] for i in range(n))
    max_val = cur
    for k in range(1, n):
        cur += total - n * nums[n - k]
        max_val = max(max_val, cur)
    return max_val