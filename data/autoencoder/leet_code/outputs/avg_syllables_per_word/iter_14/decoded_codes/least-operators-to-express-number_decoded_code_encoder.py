class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(target: int) -> int:
            if target == 0:
                return -1
            if target < x:
                # Either using '+' target times, each cost 2 minus 1 (no leading operator),
                # or using '-' (x - target) times
                return min(2 * target - 1, 2 * (x - target))
            power = 1
            while x ** power <= target:
                power += 1
            power -= 1
            base = x ** power
            res = dp(target - base) + power
            if base * x - target < target:
                res = min(res, dp(base * x - target) + power + 1)
            return res

        return dp(target)