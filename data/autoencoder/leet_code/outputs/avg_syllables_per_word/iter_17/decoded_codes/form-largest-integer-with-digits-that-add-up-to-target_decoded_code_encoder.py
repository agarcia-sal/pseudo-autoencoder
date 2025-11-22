class Solution:
    def largestNumber(self, cost, target):
        cost_to_digit = self.build_cost_to_digit_mapping(cost)
        dp = self.initialize_dp_array(target)

        for t in range(1, target + 1):
            for cost_value, digit in cost_to_digit.items():
                if t >= cost_value and dp[t - cost_value] != -1:
                    candidate_number = digit + dp[t - cost_value]
                    if dp[t] == -1 or len(candidate_number) > len(dp[t]) or (len(candidate_number) == len(dp[t]) and candidate_number > dp[t]):
                        dp[t] = candidate_number

        return dp[target] if dp[target] != -1 else "0"

    def build_cost_to_digit_mapping(self, cost):
        mapping = {}
        for index, cost_value in enumerate(cost):
            mapping[cost_value] = str(index + 1)
        return mapping

    def initialize_dp_array(self, target):
        dp = [""]
        for _ in range(1, target + 1):
            dp.append(-1)
        return dp