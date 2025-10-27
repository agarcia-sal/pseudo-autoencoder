class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def dp(t: int) -> int:
            if t == 0:
                return -1
            if t < x:
                return min(2 * t - 1, 2 * (x - t))
            power = 1
            while x ** power <= t:
                power += 1
            power -= 1
            res = dp(t - x ** power) + power
            # Check if approaching from the next power is better
            diff = x ** (power + 1) - t
            if diff < t:
                res = min(res, dp(diff) + power + 1)
            return res

        return dp(target)