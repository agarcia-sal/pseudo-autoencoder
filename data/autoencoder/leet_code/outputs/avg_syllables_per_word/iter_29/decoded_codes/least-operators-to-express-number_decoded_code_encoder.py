class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def dp(target: int) -> int:
            if target == 0:
                return -1
            if target < x:
                return min(2 * target - 1, 2 * x - target)

            power = 1
            while pow(x, power) <= target:
                power += 1
            power -= 1

            res = dp(target - pow(x, power)) + power
            if pow(x, power + 1) - target < target:
                res = min(res, dp(pow(x, power + 1) - target) + power + 1)
            return res

        return dp(target)