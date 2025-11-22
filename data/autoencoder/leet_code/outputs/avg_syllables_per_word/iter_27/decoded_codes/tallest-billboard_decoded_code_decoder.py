from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                candidate_key_one = d + rod
                if candidate_key_one not in new_dp or new_dp[candidate_key_one] < y:
                    new_dp[candidate_key_one] = y

                absolute_difference = d - rod
                if absolute_difference < 0:
                    absolute_difference = rod - d

                candidate_key_two = absolute_difference
                candidate_value_two = y + min(d, rod)
                if candidate_key_two not in new_dp or new_dp[candidate_key_two] < candidate_value_two:
                    new_dp[candidate_key_two] = candidate_value_two
            dp = new_dp
        return dp.get(0, 0)