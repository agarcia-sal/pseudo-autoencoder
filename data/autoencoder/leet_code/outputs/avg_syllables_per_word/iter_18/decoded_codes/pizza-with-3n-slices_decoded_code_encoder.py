class Solution:
    def maxSizeSlices(self, slices):
        n = len(slices) // 3

        from functools import lru_cache

        @lru_cache(None)
        def dp(start, end, k):
            if k == 0 or start > end:
                return 0
            # pick the current slice and move two steps forward
            pick = slices[start] + dp(start + 2, end, k - 1)
            # skip the current slice and move one step forward
            skip = dp(start + 1, end, k)
            return max(pick, skip)

        case1 = dp(1, len(slices) - 1, n)
        case2 = dp(0, len(slices) - 2, n)
        return max(case1, case2)