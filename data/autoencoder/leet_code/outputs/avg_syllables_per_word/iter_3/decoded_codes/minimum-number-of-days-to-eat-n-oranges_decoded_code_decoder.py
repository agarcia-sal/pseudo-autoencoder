from functools import cache

class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dp(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            return 1 + min(remaining % 2 + dp(remaining // 2), remaining % 3 + dp(remaining // 3))
        return dp(n)