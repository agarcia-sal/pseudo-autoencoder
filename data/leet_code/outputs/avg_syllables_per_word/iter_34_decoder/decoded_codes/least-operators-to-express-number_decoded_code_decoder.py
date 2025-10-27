class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def dp(target_inner: int) -> int:
            if target_inner == 0:
                return -1
            if target_inner < x:
                return min(2 * target_inner - 1, 2 * (x - target_inner))

            power = 1
            while x ** power <= target_inner:
                power += 1
            power -= 1

            result = dp(target_inner - x ** power) + power
            next_power_diff = x ** (power + 1) - target_inner
            if next_power_diff < target_inner:
                result = min(result, dp(next_power_diff) + power + 1)
            return result

        return dp(target)