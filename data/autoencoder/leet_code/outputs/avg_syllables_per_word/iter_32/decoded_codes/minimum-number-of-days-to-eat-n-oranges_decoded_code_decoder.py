class Solution:
    def minDays(self, n: int) -> int:
        def dp(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            # Calculate days by removing 1 or 2 to make divisible by 2 or 3, plus recursion on the quotient
            return 1 + min(remaining % 2 + dp(remaining // 2), remaining % 3 + dp(remaining // 3))
        return dp(n)