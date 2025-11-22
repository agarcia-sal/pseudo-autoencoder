from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return -1
            if t < x:
                return min(2 * t - 1, 2 * x - t)
            power = 0
            while x ** (power + 1) <= t:
                power += 1
            res = dp(t - x ** power) + power
            next_diff = x ** (power + 1) - t
            if next_diff < t:
                res = min(res, dp(next_diff) + power + 1)
            return res
        return dp(target)