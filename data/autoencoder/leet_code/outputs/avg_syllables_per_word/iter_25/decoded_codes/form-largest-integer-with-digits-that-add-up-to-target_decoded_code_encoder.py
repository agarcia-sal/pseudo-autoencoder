class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        # Map each cost to its corresponding digit as a string (1-based index)
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}
        dp = ["-" * target] * (target + 1)
        dp = [""] + ["-" * target] * target  # dp[0] = "", rest are placeholder "-"

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != "-" * target:
                    candidate = d + dp[t - c]
                    if (dp[t] == "-" * target or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-" * target else "0"