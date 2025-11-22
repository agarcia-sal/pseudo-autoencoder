from math import inf
from functools import lru_cache

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)
        for i in range(n):
            for mask in range(1 << i):
                subset_sums[mask | (1 << i)] = subset_sums[mask] + jobs[i]

        @lru_cache(None)
        def dp(k, mask):
            if k == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                res = min(res, max(dp(k - 1, mask ^ submask), subset_sums[submask]))
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)