class Solution:
    def largestNumber(self, cost, target):
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}
        impossible = "-1"
        dp = [""] + [impossible] * target

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != impossible:
                    candidate = d + dp[t - c]
                    if dp[t] == impossible or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate

        return dp[target] if dp[target] != impossible else "0"