from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)

        # Precompute sums of all subsets using dynamic programming on bitmasks
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        def dp(k_param, mask):
            if k_param == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                # max of dp(k_param-1, mask ^ submask) and sum of submask subset
                val = max(dp(k_param - 1, mask ^ submask), subset_sums[submask])
                if val < res:
                    res = val
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)