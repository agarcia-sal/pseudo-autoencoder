class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            return 1 + min(
                remaining % 2 + dp(remaining // 2),
                remaining % 3 + dp(remaining // 3)
            )

        return dp(n)