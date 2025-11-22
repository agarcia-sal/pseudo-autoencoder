from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_digit = {}
        for index in range(len(cost)):
            current_cost = cost[index]
            corresponding_digit = str(index + 1)
            cost_to_digit[current_cost] = corresponding_digit

        dp = ['-1'] + ['-1'] * target
        dp[0] = ''

        for number_t in range(1, target + 1):
            for key_cost, value_digit in cost_to_digit.items():
                if number_t >= key_cost and dp[number_t - key_cost] != '-1':
                    candidate = value_digit + dp[number_t - key_cost]
                    current_dp = dp[number_t]
                    # Update if dp[number_t] is '-1' or candidate is longer or candidate equal length but lex greater
                    if (current_dp == '-1' or
                        len(candidate) > len(current_dp) or
                        (len(candidate) == len(current_dp) and candidate > current_dp)):
                        dp[number_t] = candidate

        return dp[target] if dp[target] != '-1' else '0'