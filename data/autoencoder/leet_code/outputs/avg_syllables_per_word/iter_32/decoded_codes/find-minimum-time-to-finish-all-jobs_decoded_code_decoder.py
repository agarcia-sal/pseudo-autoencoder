from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        # Precompute sums of all subsets of jobs
        subset_sums = [0] * (1 << n)
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        from math import inf
        from functools import lru_cache

        @lru_cache(None)
        def dp(k_remaining: int, mask: int) -> int:
            if k_remaining == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                # dp(k-1, mask ^ submask) processes rest jobs,
                # subset_sums[submask] is sum of current group
                res = min(res, max(dp(k_remaining - 1, mask ^ submask), subset_sums[submask]))
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)