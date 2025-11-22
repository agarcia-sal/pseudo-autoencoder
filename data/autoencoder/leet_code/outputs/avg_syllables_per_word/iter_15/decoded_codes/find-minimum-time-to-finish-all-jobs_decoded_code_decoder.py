from typing import List
import math
from functools import lru_cache

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        subset_sums = [0] * (1 << n)

        for i in range(n):
            for mask in range(1 << i):
                subset_sums[mask | (1 << i)] = subset_sums[mask] + jobs[i]

        @lru_cache(None)
        def dp(k_left: int, mask: int) -> int:
            if k_left == 1:
                return subset_sums[mask]

            res = math.inf
            submask = mask
            while submask > 0:
                temp = max(dp(k_left - 1, mask ^ submask), subset_sums[submask])
                if temp < res:
                    res = temp
                submask = (submask - 1) & mask

            return res

        return dp(k, (1 << n) - 1)