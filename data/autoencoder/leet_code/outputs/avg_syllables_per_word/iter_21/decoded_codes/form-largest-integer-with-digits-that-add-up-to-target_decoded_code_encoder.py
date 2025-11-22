class Solution:
    def largestNumber(self, cost, target):
        cost_to_digit = self.conversion(cost)
        dp = self.initialize_dp_array(target)
        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                c = int(c)
                if t >= c and dp[t - c] != "-1":
                    candidate = d + dp[t - c]
                    if dp[t] == "-1" or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate
        return dp[target] if dp[target] != "-1" else "0"

    def conversion(self, cost):
        result = {}
        for index in range(len(cost)):
            key = cost[index]
            value = str(index + 1)
            result[key] = value
        return result

    def initialize_dp_array(self, target):
        # dp[0] = "" means zero target has an empty number string
        # all other dp elements initialized to "-1" meaning no solution yet
        dp_array = [""] + ["-1"] * target
        return dp_array