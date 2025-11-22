from functools import lru_cache

class Solution:
    def maxSizeSlices(self, slices):
        n = len(slices) // 3

        @lru_cache(None)
        def dp(start, end, k):
            if k == 0 or start > end:
                return 0
            pick = slices[start] + dp(start + 2, end, k - 1)
            skip = dp(start + 1, end, k)
            return max(pick, skip)

        case1 = dp(1, len(slices) - 1, n)
        case2 = dp(0, len(slices) - 2, n)

        return max(case1, case2)