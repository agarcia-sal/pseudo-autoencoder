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
            while submask:
                candidate_one = dp(k - 1, mask ^ submask)
                candidate_two = subset_sums[submask]
                current_max = max(candidate_one, candidate_two)
                if current_max < res:
                    res = current_max
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)