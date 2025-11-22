from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(k_remain, mask):
            if k_remain == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                candidate1 = dp(k_remain - 1, mask ^ submask)
                candidate2 = subset_sums[submask]
                current_max = candidate1 if candidate1 > candidate2 else candidate2
                if current_max < res:
                    res = current_max
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)