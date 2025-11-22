class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return -1  # represents no operation needed

            if t < x:
                # Use either t times x^0 (which is 1) with t-1 additions: cost = 2*t - 1
                # Or (x - t) times subtractions from x^1: cost = 2*x - t
                return min(2 * t - 1, 2 * x - t)

            power = 0
            while x ** power <= t:
                power += 1
            power -= 1

            res = dp(t - x ** power) + power  # power times operator cost

            leftover = x ** (power + 1) - t
            if leftover < t:
                candidate = dp(leftover) + power + 1
                if candidate < res:
                    res = candidate

            return res

        return dp(target)