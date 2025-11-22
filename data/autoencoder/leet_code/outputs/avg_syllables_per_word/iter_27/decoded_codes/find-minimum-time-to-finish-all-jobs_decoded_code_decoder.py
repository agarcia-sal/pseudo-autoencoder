from math import inf
from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        subset_sums = [0] * (1 << n)

        for i in range(n):
            bit = 1 << i
            for mask in range(bit):
                subset_sums[mask | bit] = subset_sums[mask] + jobs[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(k_remain: int, mask: int) -> int:
            if k_remain == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask > 0:
                candidate = max(dp(k_remain - 1, mask ^ submask), subset_sums[submask])
                if candidate < res:
                    res = candidate
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)