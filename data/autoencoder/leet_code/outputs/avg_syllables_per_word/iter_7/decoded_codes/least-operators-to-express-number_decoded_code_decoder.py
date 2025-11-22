from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dp(target: int) -> int:
            if target == 0:
                return -1
            if target < x:
                return min(2 * target - 1, 2 * (x - target))
            power = 1
            while x ** power <= target:
                power += 1
            power -= 1
            res = dp(target - x ** power) + power
            if (x ** (power + 1) - target) < target:
                res = min(res, dp(x ** (power + 1) - target) + power + 1)
            return res

        return dp(target)