from typing import List, Dict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp: Dict[int, int] = {0: 0}  # key: difference, value: max sum of smaller support
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                # Taller support: difference increases by rod length
                key_for_taller_support = d + rod
                if key_for_taller_support in new_dp:
                    new_dp_value = new_dp[key_for_taller_support]
                else:
                    new_dp_value = 0
                if y > new_dp_value:
                    new_dp[key_for_taller_support] = y

                # Shorter support: difference changes by absolute difference between d and rod
                absolute_difference = d - rod
                if absolute_difference < 0:
                    absolute_difference = rod - d

                value_for_shorter_support = y + min(d, rod)
                if absolute_difference in new_dp:
                    new_dp_value2 = new_dp[absolute_difference]
                else:
                    new_dp_value2 = 0
                if value_for_shorter_support > new_dp_value2:
                    new_dp[absolute_difference] = value_for_shorter_support
            dp = new_dp
        return dp.get(0, 0)