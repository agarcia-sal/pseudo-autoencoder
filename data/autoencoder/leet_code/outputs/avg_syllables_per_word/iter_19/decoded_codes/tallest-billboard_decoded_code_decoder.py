from collections import defaultdict
import copy

class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                # Add rod to taller support
                sum_with_rod_added_to_taller_support = d + rod
                if sum_with_rod_added_to_taller_support not in new_dp or new_dp[sum_with_rod_added_to_taller_support] < y:
                    new_dp[sum_with_rod_added_to_taller_support] = y

                # Add rod to shorter support
                difference_after_adding_rod_to_shorter_support = abs(d - rod)
                candidate_value = y + min(d, rod)
                if difference_after_adding_rod_to_shorter_support not in new_dp or new_dp[difference_after_adding_rod_to_shorter_support] < candidate_value:
                    new_dp[difference_after_adding_rod_to_shorter_support] = candidate_value

            dp = new_dp
        return dp.get(0, 0)