from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)

        subset_sums = self.initialize_subset_sums(n, jobs)

        from functools import lru_cache

        @lru_cache(None)
        def dp(k_parameter, mask_parameter):
            if k_parameter == 1:
                return subset_sums[mask_parameter]

            result = inf
            submask = mask_parameter
            while submask:
                candidate_one = dp(k_parameter - 1, mask_parameter ^ submask)
                candidate_two = subset_sums[submask]
                candidate_max = max(candidate_one, candidate_two)
                if candidate_max < result:
                    result = candidate_max
                submask = (submask - 1) & mask_parameter

            return result

        return dp(k, (1 << n) - 1)

    def initialize_subset_sums(self, n, jobs):
        length = 1 << n
        subset_sums = [0] * length
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]
        return subset_sums