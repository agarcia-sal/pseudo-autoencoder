from functools import cache

def maximumANDSum(nums, n):
    @cache
    def dp(i, s):
        if i == len(nums):
            return 0
        return max(
            (nums[i] & (j + 1)) + dp(i + 1, s[:j] + (s[j] + 1,) + s[j + 1:])
            for j in range(n) if s[j] < 2
        )
    return dp(0, (0,) * n)