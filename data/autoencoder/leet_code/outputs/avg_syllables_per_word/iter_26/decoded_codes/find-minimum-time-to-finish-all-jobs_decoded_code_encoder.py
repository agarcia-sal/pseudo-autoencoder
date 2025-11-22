from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)

        # Precompute sums of all subsets of jobs
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        def dp(k_parameter, mask_parameter):
            if k_parameter == 1:
                return subset_sums[mask_parameter]
            res = inf

            submask = mask_parameter
            while submask:
                res = min(res, max(dp(k_parameter - 1, mask_parameter ^ submask), subset_sums[submask]))
                submask = (submask - 1) & mask_parameter

            return res

        return dp(k, (1 << n) - 1)