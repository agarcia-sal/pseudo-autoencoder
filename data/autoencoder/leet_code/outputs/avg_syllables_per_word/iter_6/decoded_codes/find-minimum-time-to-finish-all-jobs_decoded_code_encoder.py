class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)
        for i in range(n):
            for mask in range(1 << i):
                subset_sums[mask | (1 << i)] = subset_sums[mask] + jobs[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(k, mask):
            if k == 1:
                return subset_sums[mask]
            res = float('inf')
            submask = mask
            while submask:
                temp = max(dp(k - 1, mask ^ submask), subset_sums[submask])
                if temp < res:
                    res = temp
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)