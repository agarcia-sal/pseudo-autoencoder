from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Map each cost value to its digit string, digits are '1' through len(cost)
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}

        # Initialize dp where dp[t] holds the largest number (as string) with cost t
        # dp[0] is empty string (cost 0, no digits), others are "-1" meaning no number formed
        dp = ["-1"] * (target + 1)
        dp[0] = ""

        for t in range(1, target + 1):
            for cost_value, digit_str in cost_to_digit.items():
                if t >= cost_value and dp[t - cost_value] != "-1":
                    candidate = digit_str + dp[t - cost_value]  # prepend digit to form potentially larger number
                    # Update if dp[t] is "-1" or candidate is longer or same length but lex greater
                    if (dp[t] == "-1" or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-1" else "0"