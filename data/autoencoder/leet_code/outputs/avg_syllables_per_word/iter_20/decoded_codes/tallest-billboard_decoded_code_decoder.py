from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_pos = d + rod
                if sum_pos not in new_dp or new_dp[sum_pos] < y:
                    new_dp[sum_pos] = y
                diff_pos = abs(d - rod)
                smaller = min(d, rod)
                if diff_pos not in new_dp or new_dp[diff_pos] < y + smaller:
                    new_dp[diff_pos] = y + smaller
            dp = new_dp
        return dp.get(0, 0)