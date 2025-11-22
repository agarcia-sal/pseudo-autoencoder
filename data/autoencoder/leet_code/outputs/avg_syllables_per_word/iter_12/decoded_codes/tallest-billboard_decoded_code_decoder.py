class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                sum_for_taller_support = d + rod
                current_max_for_taller_support = new_dp.get(sum_for_taller_support, 0)
                updated_max_for_taller_support = max(current_max_for_taller_support, y)
                new_dp[sum_for_taller_support] = updated_max_for_taller_support

                difference_for_shorter_support = abs(d - rod)
                current_max_for_shorter_support = new_dp.get(difference_for_shorter_support, 0)
                additional_height_for_shorter_support = y + min(d, rod)
                updated_max_for_shorter_support = max(current_max_for_shorter_support, additional_height_for_shorter_support)
                new_dp[difference_for_shorter_support] = updated_max_for_shorter_support
            dp = new_dp
        return dp.get(0, 0)