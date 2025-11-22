from typing import List
from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                # Add rod to the taller support
                key_for_taller_support = d + rod
                value_for_taller_support = max(new_dp.get(key_for_taller_support, 0), y)
                new_dp[key_for_taller_support] = value_for_taller_support

                # Calculate difference key for shorter support update
                if d > rod:
                    difference_key = d - rod
                elif rod > d:
                    difference_key = rod - d
                else:
                    difference_key = 0

                # Minimum value to add to shorter support
                minimum_value = d if d < rod else rod

                value_for_shorter_support = max(new_dp.get(difference_key, 0), y + minimum_value)
                new_dp[difference_key] = value_for_shorter_support

            dp = new_dp

        return dp.get(0, 0)