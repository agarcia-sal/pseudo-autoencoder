def minPatches(nums, n):
    missing = 1
    patches = 0
    i = 0
    while missing <= n:
        if i < len(nums) and nums[i] <= missing:
            missing += nums[i]
            i += 1
        else:
            missing += missing
            patches += 1
    return patches