from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_key_taller = d + rod
                current_max_taller = new_dp.get(sum_key_taller, 0)
                updated_max_taller = max(current_max_taller, y)
                new_dp[sum_key_taller] = updated_max_taller

                absolute_difference = abs(d - rod)
                current_max_shorter = new_dp.get(absolute_difference, 0)
                sum_shorter = y + min(d, rod)
                updated_max_shorter = max(current_max_shorter, sum_shorter)
                new_dp[absolute_difference] = updated_max_shorter
            dp = new_dp
        return dp.get(0, 0)