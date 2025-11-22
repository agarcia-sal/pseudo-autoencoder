from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dp(target_inner: int) -> int:
            if target_inner == 0:
                return -1
            if target_inner < x:
                return min(2 * target_inner - 1, 2 * x - target_inner)
            power = 1
            while x ** power <= target_inner:
                power += 1
            power -= 1

            res = dp(target_inner - x ** power) + power
            if x ** (power + 1) - target_inner < target_inner:
                res = min(res, dp(x ** (power + 1) - target_inner) + power + 1)
            return res

        return dp(target)