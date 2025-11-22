from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                new_dp[d + rod] = max(new_dp.get(d + rod, 0), y)
                diff = abs(d - rod)
                candidate = y + min(d, rod)
                new_dp[diff] = max(new_dp.get(diff, 0), candidate)
            dp = new_dp
        return dp.get(0, 0)