class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            # Cost of reducing by dividing by 2 plus cost of remainder
            cost_div2 = (remaining % 2) + dp(remaining // 2)
            # Cost of reducing by dividing by 3 plus cost of remainder
            cost_div3 = (remaining % 3) + dp(remaining // 3)
            return 1 + min(cost_div2, cost_div3)

        return dp(n)