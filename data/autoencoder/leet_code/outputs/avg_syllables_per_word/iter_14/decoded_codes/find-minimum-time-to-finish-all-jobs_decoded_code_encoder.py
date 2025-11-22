from math import inf

class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        n = len(jobs)
        subset_sums = [0] * (1 << n)

        # Precompute the sums of all subsets of jobs
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        memo = {}

        def dp(k: int, mask: int) -> int:
            if k == 1:
                return subset_sums[mask]
            if (k, mask) in memo:
                return memo[(k, mask)]

            res = inf
            submask = mask
            while submask > 0:
                # candidate is max of dp(k-1, mask-submask) and sum of submask subset
                candidate = max(dp(k - 1, mask ^ submask), subset_sums[submask])
                if candidate < res:
                    res = candidate
                submask = (submask - 1) & mask

            memo[(k, mask)] = res
            return res

        full_mask = (1 << n) - 1
        return dp(k, full_mask)