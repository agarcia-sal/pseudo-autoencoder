class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_one = d + rod
                if sum_one not in new_dp or new_dp[sum_one] < y:
                    new_dp[sum_one] = y
                diff = abs(d - rod)
                min_value = min(d, rod)
                new_value = y + min_value
                if diff not in new_dp or new_dp[diff] < new_value:
                    new_dp[diff] = new_value
            dp = new_dp
        return dp.get(0, 0)