from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                key_for_taller_support = d + rod
                value_for_taller_support = max(new_dp.get(key_for_taller_support, 0), y)
                new_dp[key_for_taller_support] = value_for_taller_support

                absolute_difference = abs(d - rod)
                value_for_shorter_support = max(new_dp.get(absolute_difference, 0), y + min(d, rod))
                new_dp[absolute_difference] = value_for_shorter_support

            dp = new_dp
        return dp.get(0, 0)