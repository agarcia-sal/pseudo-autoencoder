def jump(nums):
    if len(nums) <= 1:
        return 0
    j, end, far = 0, 0, 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == end:
            j += 1
            end = far
            if end >= len(nums) - 1:
                break
    return j