class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import cache

        @cache
        def dp(t: int) -> int:
            if t == 0:
                return -1
            if t < x:
                return min(2 * t - 1, 2 * (x - t))

            power = 0
            while x ** (power + 1) <= t:
                power += 1

            res = dp(t - x ** power) + power
            high_rem = x ** (power + 1) - t
            if high_rem < t:
                res = min(res, dp(high_rem) + power + 1)
            return res

        return dp(target)