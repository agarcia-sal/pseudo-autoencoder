def minDays(n):
    from functools import cache

    @cache
    def dp(remaining):
        if remaining <= 1:
            return remaining
        return 1 + min(remaining % 2 + dp(remaining // 2), remaining % 3 + dp(remaining // 3))

    return dp(n)