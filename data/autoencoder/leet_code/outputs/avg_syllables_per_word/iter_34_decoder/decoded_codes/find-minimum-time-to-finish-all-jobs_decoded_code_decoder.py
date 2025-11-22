from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        memo = {}
        def dp(k_param, mask_param):
            if k_param == 1:
                return subset_sums[mask_param]
            if (k_param, mask_param) in memo:
                return memo[(k_param, mask_param)]

            res = inf
            submask = mask_param
            while submask:
                # Minimize the max load between one subset and remaining subsets
                current = max(dp(k_param - 1, mask_param ^ submask), subset_sums[submask])
                if current < res:
                    res = current
                submask = (submask - 1) & mask_param

            memo[(k_param, mask_param)] = res
            return res

        return dp(k, (1 << n) - 1)