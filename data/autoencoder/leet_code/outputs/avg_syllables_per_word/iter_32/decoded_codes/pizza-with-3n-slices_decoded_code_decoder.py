from functools import lru_cache
from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3

        @lru_cache(None)
        def dp(start: int, end: int, k: int) -> int:
            if k == 0 or start > end:
                return 0
            # Pick the current slice and skip the next one
            pick = slices[start] + dp(start + 2, end, k - 1)
            # Skip the current slice
            skip = dp(start + 1, end, k)
            return max(pick, skip)

        case1 = dp(1, len(slices) - 1, n)
        case2 = dp(0, len(slices) - 2, n)
        return max(case1, case2)