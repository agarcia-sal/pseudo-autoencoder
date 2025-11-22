from functools import cache

class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dp(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            option1 = remaining % 2 + dp(remaining // 2)
            option2 = remaining % 3 + dp(remaining // 3)
            return 1 + min(option1, option2)
        return dp(n)