class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return -1  # Base case for zero, cost is -1 to offset the +1 cost later
            if t < x:
                # Either use t times 'x/x' (cost 2 per unit minus 1 for the first) or use subtraction from x
                return min(2 * t - 1, 2 * x - 2 * t)
            power = 0
            while x ** (power + 1) <= t:
                power += 1
            p_val = x ** power
            res = dp(t - p_val) + power  # Use x^power once (cost = power operators)
            next_p_val = p_val * x
            if next_p_val - t < t:
                res = min(res, dp(next_p_val - t) + power + 1)  # Use x^(power+1) and subtract (one extra operator)
            return res

        return dp(target)