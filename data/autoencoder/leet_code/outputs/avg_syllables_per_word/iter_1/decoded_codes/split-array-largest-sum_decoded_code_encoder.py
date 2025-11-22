def splitArray(nums, k):
    def canSplit(maxSum):
        total, subs = 0, 1
        for n in nums:
            if total + n > maxSum:
                subs += 1
                total = n
            else:
                total += n
        return subs <= k

    l, r = max(nums), sum(nums)
    while l < r:
        m = (l + r) // 2
        if canSplit(m):
            r = m
        else:
            l = m + 1
    return l