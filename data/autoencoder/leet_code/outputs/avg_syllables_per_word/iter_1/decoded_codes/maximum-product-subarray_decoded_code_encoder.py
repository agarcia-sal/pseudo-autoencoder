def maxProduct(nums):
    if not nums:
        return 0
    max_p = min_p = res = nums[0]
    for n in nums[1:]:
        if n < 0:
            max_p, min_p = min_p, max_p
        max_p = max(n, max_p * n)
        min_p = min(n, min_p * n)
        res = max(res, max_p)
    return res