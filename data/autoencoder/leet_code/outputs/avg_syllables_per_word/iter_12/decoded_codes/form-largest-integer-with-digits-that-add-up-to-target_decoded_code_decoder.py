class Solution:
    def largestNumber(self, cost, target):
        cost_to_digit = {}
        for i, c in enumerate(cost):
            digit_string = str(i + 1)
            cost_to_digit[c] = digit_string

        dp = [''] + ['-1'] * target

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != '-1':
                    candidate = d + dp[t - c]
                    if (dp[t] == '-1' or
                        len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        dp[t] = candidate

        return dp[target] if dp[target] != '-1' else '0'