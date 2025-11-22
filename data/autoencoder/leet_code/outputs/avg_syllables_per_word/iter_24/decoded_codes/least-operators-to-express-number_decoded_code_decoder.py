class Solution:
    def leastOpsExpressTarget(self, x, target):
        def dp(target):
            if target == 0:
                return -1
            if target < x:
                return min(2 * target - 1, 2 * (x - target))
            power = 1
            while x ** power <= target:
                power += 1
            power -= 1
            res = dp(target - x ** power) + power
            if x ** (power + 1) - target < target:
                res = min(res, dp(x ** (power + 1) - target) + power + 1)
            return res
        return dp(target)