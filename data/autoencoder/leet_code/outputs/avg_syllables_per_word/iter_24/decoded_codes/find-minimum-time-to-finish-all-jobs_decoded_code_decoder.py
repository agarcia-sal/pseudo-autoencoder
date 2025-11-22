from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        total_subsets = 1 << n
        subset_sums = [0] * total_subsets
        for i in range(n):
            bit = 1 << i
            limit = bit
            for mask in range(limit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(k, mask):
            if k == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                candidate = max(dp(k - 1, mask ^ submask), subset_sums[submask])
                if candidate < res:
                    res = candidate
                submask = (submask - 1) & mask
            return res

        return dp(k, total_subsets - 1)