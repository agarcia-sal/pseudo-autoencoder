def find_min(nums):
    L, R = 0, len(nums) - 1
    if nums[L] < nums[R]:
        return nums[L]
    while L < R:
        M = (L + R) // 2
        if nums[M] > nums[R]:
            L = M + 1
        else:
            R = M
    return nums[L]