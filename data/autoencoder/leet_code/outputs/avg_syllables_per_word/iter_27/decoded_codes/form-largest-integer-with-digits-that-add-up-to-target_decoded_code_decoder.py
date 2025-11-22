from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}
        dp = ["-" for _ in range(target + 1)]
        dp[0] = ""

        for t in range(1, target + 1):
            for cost_key, digit_value in cost_to_digit.items():
                if t >= cost_key and dp[t - cost_key] != "-":
                    candidate = digit_value + dp[t - cost_key]
                    if (
                        dp[t] == "-"
                        or len(candidate) > len(dp[t])
                        or (len(candidate) == len(dp[t]) and candidate > dp[t])
                    ):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-" else "0"