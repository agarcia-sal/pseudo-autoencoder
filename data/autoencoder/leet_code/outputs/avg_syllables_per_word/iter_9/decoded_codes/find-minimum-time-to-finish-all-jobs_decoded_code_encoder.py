class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)

        def subset_sums_initializer():
            subset_sums = [0] * (1 << n)
            for i in range(n):
                for mask in range(1 << i):
                    subset_sums[mask | (1 << i)] = subset_sums[mask] + jobs[i]
            return subset_sums

        subset_sums = subset_sums_initializer()

        from functools import lru_cache

        @lru_cache(None)
        def dp(k_param, mask_param):
            if k_param == 1:
                return subset_sums[mask_param]
            res = float('inf')
            submask = mask_param
            while submask:
                candidate = max(dp(k_param - 1, mask_param ^ submask), subset_sums[submask])
                if candidate < res:
                    res = candidate
                submask = (submask - 1) & mask_param
            return res

        return dp(k, (1 << n) - 1)