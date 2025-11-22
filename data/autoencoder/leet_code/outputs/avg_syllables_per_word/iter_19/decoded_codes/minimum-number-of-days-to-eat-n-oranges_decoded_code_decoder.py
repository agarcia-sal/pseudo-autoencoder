class Solution:
    def minDays(self, n):
        from functools import lru_cache

        @lru_cache(None)
        def dp(remaining):
            if remaining <= 1:
                return remaining
            # Days to reduce by dividing by 2 or 3 plus the cost for the quotient
            res = 1 + min(
                (remaining % 2) + dp(remaining // 2),
                (remaining % 3) + dp(remaining // 3)
            )
            return res

        return dp(n)