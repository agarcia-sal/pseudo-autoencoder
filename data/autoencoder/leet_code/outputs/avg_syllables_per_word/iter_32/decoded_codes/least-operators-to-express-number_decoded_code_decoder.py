from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return -1  # base case

            if t < x:
                # Min between expressing t as sum of ones (using + t times and - (x - t) times)
                return min(2 * t - 1, 2 * x - 2 * t)

            power = 0
            while x ** (power + 1) <= t:
                power += 1

            # Express as x^power plus remainder
            res = dp(t - x**power) + power

            # Alternative: express as x^(power + 1) minus remainder
            if x**(power + 1) - t < t:
                res = min(res, dp(x**(power + 1) - t) + power + 1)

            return res

        return dp(target)