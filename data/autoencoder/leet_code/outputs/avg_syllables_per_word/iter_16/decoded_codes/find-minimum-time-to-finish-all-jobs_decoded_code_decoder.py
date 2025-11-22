from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = [0] * (1 << n)

        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        def dp(k, mask):
            if k == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask > 0:
                temp_max = max(dp(k - 1, mask ^ submask), subset_sums[submask])
                if temp_max < res:
                    res = temp_max
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)