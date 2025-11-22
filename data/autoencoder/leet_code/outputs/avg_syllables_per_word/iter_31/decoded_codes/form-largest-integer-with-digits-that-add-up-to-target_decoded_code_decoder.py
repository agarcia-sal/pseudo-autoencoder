from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Map each cost to the corresponding digit (as string)
        cost_to_digit = {}
        for index in range(len(cost)):
            key_cost = cost[index]
            value_digit = str(index + 1)
            # If multiple digits have the same cost, keep the one with larger digit for lex order
            if key_cost not in cost_to_digit or value_digit > cost_to_digit[key_cost]:
                cost_to_digit[key_cost] = value_digit

        impossible = '#'
        # dp[t] holds the largest number (string) that can be formed with total cost t
        dp = ["" if t == 0 else impossible for t in range(target + 1)]

        for t in range(1, target + 1):
            for key_cost, value_digit in cost_to_digit.items():
                if t >= key_cost and dp[t - key_cost] != impossible:
                    candidate = value_digit + dp[t - key_cost]
                    current = dp[t]
                    # Update dp[t] if candidate is better:
                    # 1) dp[t] is impossible
                    # 2) candidate has longer length
                    # 3) candidate has equal length but lex greater
                    if current == impossible or len(candidate) > len(current) or (len(candidate) == len(current) and candidate > current):
                        dp[t] = candidate

        if dp[target] != impossible:
            # Digits were added with new digits in front, but ordering by largest digit first is correct
            # So just return dp[target]
            return dp[target]
        else:
            return "0"