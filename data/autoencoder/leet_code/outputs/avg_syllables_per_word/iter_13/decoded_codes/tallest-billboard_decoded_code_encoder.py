class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                key_added_to_taller = d + rod
                if key_added_to_taller in new_dp:
                    new_dp[key_added_to_taller] = max(new_dp[key_added_to_taller], y)
                else:
                    new_dp[key_added_to_taller] = y

                difference_after_subtraction = abs(d - rod)
                min_between_d_and_rod = min(d, rod)
                new_value = y + min_between_d_and_rod
                if difference_after_subtraction in new_dp:
                    new_dp[difference_after_subtraction] = max(new_dp[difference_after_subtraction], new_value)
                else:
                    new_dp[difference_after_subtraction] = new_value

            dp = new_dp

        return dp.get(0, 0)