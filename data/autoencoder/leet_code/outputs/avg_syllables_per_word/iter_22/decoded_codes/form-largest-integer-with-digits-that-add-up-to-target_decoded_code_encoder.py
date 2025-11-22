from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_digit = {}
        for i, c in enumerate(cost):
            # Map cost to the corresponding digit string (1-based)
            cost_to_digit[c] = str(i + 1)

        # Initialize dp array with "" at dp[0] and "-" * target for all others
        dp = [""] + ["-" * target for _ in range(target)]

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != "-" * target:
                    candidate = d + dp[t - c]
                    if (dp[t] == "-" * target or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-" * target else "0"