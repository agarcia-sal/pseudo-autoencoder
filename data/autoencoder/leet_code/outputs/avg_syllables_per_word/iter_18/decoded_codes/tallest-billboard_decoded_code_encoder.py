class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_for_taller = d + rod
                if sum_for_taller in new_dp:
                    if y > new_dp[sum_for_taller]:
                        new_dp[sum_for_taller] = y
                else:
                    new_dp[sum_for_taller] = y

                difference_to_add = abs(d - rod)
                value_for_shorter = y + min(d, rod)
                if difference_to_add in new_dp:
                    if value_for_shorter > new_dp[difference_to_add]:
                        new_dp[difference_to_add] = value_for_shorter
                else:
                    new_dp[difference_to_add] = value_for_shorter
            dp = new_dp
        return dp.get(0, 0)