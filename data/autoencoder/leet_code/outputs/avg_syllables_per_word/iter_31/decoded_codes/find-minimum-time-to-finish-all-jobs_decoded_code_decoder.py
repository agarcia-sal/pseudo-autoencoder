from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        total_subsets = 1 << n  # 2**n

        # Precompute the sum of jobs for all subsets represented as bitmasks
        subset_sums = [0] * total_subsets
        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        @lru_cache(None)
        def dp(k: int, mask: int) -> int:
            if k == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                # Mask XOR submask: removes jobs assigned in submask from mask
                first_value = dp(k - 1, mask ^ submask)
                second_value = subset_sums[submask]

                # We want to minimize the max load between these two partitions
                candidate = max(first_value, second_value)
                if candidate < res:
                    res = candidate

                submask = (submask - 1) & mask
            return res

        return dp(k, total_subsets - 1)