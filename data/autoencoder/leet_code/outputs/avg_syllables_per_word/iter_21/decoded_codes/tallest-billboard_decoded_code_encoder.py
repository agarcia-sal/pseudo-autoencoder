class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_for_taller_support = d + rod
                new_dp_at_taller_support = new_dp.get(sum_for_taller_support, 0)
                value_for_taller_support = max(new_dp_at_taller_support, y)
                new_dp[sum_for_taller_support] = value_for_taller_support

                difference_absolute = abs(d - rod)
                new_dp_at_shorter_support = new_dp.get(difference_absolute, 0)
                minimum_height = d if d < rod else rod
                value_for_shorter_support = max(new_dp_at_shorter_support, y + minimum_height)
                new_dp[difference_absolute] = value_for_shorter_support

            dp = new_dp

        return dp.get(0, 0)