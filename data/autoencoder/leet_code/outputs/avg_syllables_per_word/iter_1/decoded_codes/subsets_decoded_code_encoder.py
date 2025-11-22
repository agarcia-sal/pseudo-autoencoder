def subsets(nums):
    if not nums:
        return [[]]
    w = subsets(nums[1:])
    return w + [[nums[0]] + s for s in w]