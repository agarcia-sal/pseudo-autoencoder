class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_for_taller_support = d + rod
                if sum_for_taller_support in new_dp:
                    new_dp[sum_for_taller_support] = max(new_dp[sum_for_taller_support], y)
                else:
                    new_dp[sum_for_taller_support] = y

                absolute_difference = abs(d - rod)
                sum_for_shorter_support = y + min(d, rod)
                if absolute_difference in new_dp:
                    new_dp[absolute_difference] = max(new_dp[absolute_difference], sum_for_shorter_support)
                else:
                    new_dp[absolute_difference] = sum_for_shorter_support
            dp = new_dp
        return dp.get(0, 0)