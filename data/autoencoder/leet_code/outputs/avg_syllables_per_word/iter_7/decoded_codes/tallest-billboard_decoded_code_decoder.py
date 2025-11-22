from typing import List, Dict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp: Dict[int, int] = {0: 0}

        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                # Case 1: Add rod to taller side
                new_dp[d + rod] = max(new_dp.get(d + rod, 0), y)

                # Case 2: Add rod to shorter side
                new_diff = abs(d - rod)
                new_height = y + min(d, rod)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_height)
            dp = new_dp

        return dp.get(0, 0)