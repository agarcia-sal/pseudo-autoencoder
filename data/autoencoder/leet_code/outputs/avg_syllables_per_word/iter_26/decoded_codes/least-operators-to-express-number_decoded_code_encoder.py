from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dp(target_value: int) -> int:
            if target_value == 0:
                return -1
            if target_value < x:
                first_option = 2 * target_value - 1
                second_option = 2 * x - target_value
                return min(first_option, second_option)
            power = 1
            while x ** power <= target_value:
                power += 1
            power -= 1

            result = dp(target_value - x ** power) + power

            if (x ** (power + 1) - target_value) < target_value:
                candidate = dp(x ** (power + 1) - target_value) + power + 1
                result = min(result, candidate)
            return result

        return dp(target)