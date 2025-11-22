class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(target_value: int) -> int:
            if target_value == 0:
                return -1  # base case: no operators needed for zero

            if target_value < x:
                # choose min between using target_value times x/x (cost 2*target_value - 1)
                # or (x - target_value) times 'x' (cost 2*x - target_value)
                return min(2 * target_value - 1, 2 * x - target_value)

            power = 0
            while x ** (power + 1) <= target_value:
                power += 1

            # Option 1: express target_value as x^power + remainder
            result = dp(target_value - x ** power) + power

            # Option 2: express target_value as x^(power + 1) - remainder (if beneficial)
            remainder = x ** (power + 1) - target_value
            if remainder < target_value:
                alt = dp(remainder) + power + 1
                if alt < result:
                    result = alt

            return result

        return dp(target)