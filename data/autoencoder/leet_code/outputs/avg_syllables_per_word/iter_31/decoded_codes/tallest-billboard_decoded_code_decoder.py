from typing import List, Dict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp: Dict[int, int] = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for diff, y in dp.items():
                added_to_taller = diff + rod
                if added_to_taller in new_dp:
                    if new_dp[added_to_taller] < y:
                        new_dp[added_to_taller] = y
                else:
                    new_dp[added_to_taller] = y

                abs_diff = abs(diff - rod)
                added_to_shorter = y + min(diff, rod)
                if abs_diff in new_dp:
                    if new_dp[abs_diff] < added_to_shorter:
                        new_dp[abs_diff] = added_to_shorter
                else:
                    new_dp[abs_diff] = added_to_shorter
            dp = new_dp
        return dp.get(0, 0)