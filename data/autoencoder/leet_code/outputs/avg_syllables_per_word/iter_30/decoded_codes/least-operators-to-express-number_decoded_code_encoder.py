class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(target_value: int) -> int:
            if target_value == 0:
                return -1
            if target_value < x:
                return min(2 * target_value - 1, 2 * x - target_value)
            power = 1
            while x ** power <= target_value:
                power += 1
            power -= 1
            res = dp(target_value - x**power) + power
            if x**(power + 1) - target_value < target_value:
                res = min(res, dp(x**(power + 1) - target_value) + power + 1)
            return res

        return dp(target)