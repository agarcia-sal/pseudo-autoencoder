class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def dp(parameter_target: int) -> int:
            if parameter_target == 0:
                return -1
            if parameter_target < x:
                option_one = 2 * parameter_target - 1
                option_two = 2 * x - parameter_target
                return min(option_one, option_two)
            current_power = 1
            while x ** current_power <= parameter_target:
                current_power += 1
            current_power -= 1
            choice_one_result = dp(parameter_target - x ** current_power) + current_power
            if x ** (current_power + 1) - parameter_target < parameter_target:
                choice_two_result = dp(x ** (current_power + 1) - parameter_target) + current_power + 1
                final_result = min(choice_one_result, choice_two_result)
            else:
                final_result = choice_one_result
            return final_result

        return dp(target)