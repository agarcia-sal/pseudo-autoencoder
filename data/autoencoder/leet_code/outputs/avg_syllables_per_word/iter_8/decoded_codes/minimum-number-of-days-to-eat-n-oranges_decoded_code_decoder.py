class Solution:
    def minDays(self, n):
        def dp(remaining):
            if remaining <= 1:
                return remaining
            option_one = (remaining % 2) + dp(remaining // 2)
            option_two = (remaining % 3) + dp(remaining // 3)
            return 1 + min(option_one, option_two)
        return dp(n)