class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(t):
            if t == 0:
                return -1
            if t < x:
                return min(2 * t - 1, 2 * x - t)
            power = 0
            while x ** (power + 1) <= t:
                power += 1
            res = dp(t - x ** power) + power
            if x ** (power + 1) - t < t:
                res = min(res, dp(x ** (power + 1) - t) + power + 1)
            return res

        return dp(target)