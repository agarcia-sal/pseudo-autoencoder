def min_max_subset_sum(jobs, k):
    n = len(jobs)
    subset_sums = [0] * (1 << n)
    for i in range(n):
        for mask in range(1 << i):
            subset_sums[mask | (1 << i)] = subset_sums[mask] + jobs[i]

    from math import inf
    memo = {}

    def dp(k, mask):
        if k == 1:
            return subset_sums[mask]
        if (k, mask) in memo:
            return memo[(k, mask)]
        res = inf
        submask = mask
        while submask:
            res = min(res, max(dp(k - 1, mask ^ submask), subset_sums[submask]))
            submask = (submask - 1) & mask
        memo[(k, mask)] = res
        return res

    return dp(k, (1 << n) - 1)