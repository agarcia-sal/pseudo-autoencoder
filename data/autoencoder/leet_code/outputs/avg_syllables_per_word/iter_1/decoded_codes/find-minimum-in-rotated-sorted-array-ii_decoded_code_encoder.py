def find_min(nums):
    L, R = 0, len(nums) - 1
    while L < R:
        M = (L + R) // 2
        if nums[M] > nums[R]:
            L = M + 1
        elif nums[M] < nums[R]:
            R = M
        else:
            R -= 1
    return nums[L]