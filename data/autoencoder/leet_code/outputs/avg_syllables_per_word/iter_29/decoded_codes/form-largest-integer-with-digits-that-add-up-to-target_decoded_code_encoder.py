class Solution:
    def largestNumber(self, cost, target):
        cost_to_digit = {}
        for i, c in enumerate(cost):
            cost_to_digit[c] = str(i + 1)

        dp = [""] + ["-" * (target)] * target

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != "-" * target:
                    candidate = d + dp[t - c]
                    if (dp[t] == "-" * target or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-" * target else "0"