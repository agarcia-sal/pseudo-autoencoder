from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}

        dp = ["-" * 101] * (target + 1)
        dp[0] = ""

        for t in range(1, target + 1):
            best = "-" * 101
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != "-" * 101:
                    candidate = d + dp[t - c]
                    if (len(candidate) > len(best)) or (len(candidate) == len(best) and candidate > best):
                        best = candidate
            dp[t] = best

        return dp[target] if dp[target] != "-" * 101 else "0"