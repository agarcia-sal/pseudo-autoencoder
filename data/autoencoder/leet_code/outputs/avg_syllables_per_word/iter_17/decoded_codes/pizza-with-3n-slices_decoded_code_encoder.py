class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        n = len(slices) // 3

        from functools import lru_cache

        @lru_cache(None)
        def dp(start: int, end: int, count: int) -> int:
            if count == 0 or start > end:
                return 0
            pick_current = slices[start] + dp(start + 2, end, count - 1)
            skip_current = dp(start + 1, end, count)
            return max(pick_current, skip_current)

        case_one = dp(1, len(slices) - 1, n)
        case_two = dp(0, len(slices) - 2, n)
        return max(case_one, case_two)