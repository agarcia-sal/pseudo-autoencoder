from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}
        dp = [""] + ["-" * (target + 1)] * target  # Use unique string for initialization to avoid confusions

        for t in range(1, target + 1):
            best = "-" * (t + 1)  # Initialize with a string smaller than any valid number for length t
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != "-" * (target + 1):
                    candidate = d + dp[t - c]
                    # Check length and lex order to update dp[t]
                    if (dp[t] == "-" * (target + 1) or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-" * (target + 1) else "0"