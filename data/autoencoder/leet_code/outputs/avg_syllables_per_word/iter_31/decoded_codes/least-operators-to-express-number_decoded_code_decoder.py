from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return -1
            if t < x:
                return min(2 * t - 1, 2 * x - t)

            power = 1
            while x ** power <= t:
                power += 1
            power -= 1

            res = dp(t - x ** power) + power
            leftover = x ** (power + 1) - t
            if leftover < t:
                res = min(res, dp(leftover) + power + 1)

            return res

        return dp(target)