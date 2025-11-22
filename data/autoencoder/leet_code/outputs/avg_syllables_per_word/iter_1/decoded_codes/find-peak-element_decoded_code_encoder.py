def find_peak(nums):
    L, R = 0, len(nums) - 1
    while L < R:
        M = (L + R) // 2
        if nums[M] > nums[M + 1]:
            R = M
        else:
            L = M + 1
    return L