class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            # Calculate cost by removing divisible parts by 2 and by 3 respectively
            remove_two = (remaining % 2) + dp(remaining // 2)
            remove_three = (remaining % 3) + dp(remaining // 3)
            result = 1 + min(remove_two, remove_three)
            return result

        return dp(n)