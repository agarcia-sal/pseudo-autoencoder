from math import inf

class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        subset_sums = self.initialize_subset_sums(n, jobs)

        def dp(k_parameter, mask_parameter):
            if k_parameter == 1:
                return subset_sums[mask_parameter]
            res = inf
            submask = mask_parameter
            while submask:
                current_maximum = max(
                    dp(k_parameter - 1, mask_parameter ^ submask),
                    subset_sums[submask]
                )
                if current_maximum < res:
                    res = current_maximum
                submask = (submask - 1) & mask_parameter
            return res

        return dp(k, (1 << n) - 1)

    def initialize_subset_sums(self, n_value, jobs_list):
        subset_sums_list = [0] * (1 << n_value)
        for i in range(n_value):
            for mask_value in range(1 << i):
                new_index = mask_value | (1 << i)
                subset_sums_list[new_index] = subset_sums_list[mask_value] + jobs_list[i]
        return subset_sums_list