from typing import List
from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                new_key_taller = d + rod
                new_dp[new_key_taller] = max(new_dp.get(new_key_taller, 0), y)

                new_key_shorter = abs(d - rod)
                new_value_shorter = y + min(d, rod)
                new_dp[new_key_shorter] = max(new_dp.get(new_key_shorter, 0), new_value_shorter)
            dp = new_dp
        return dp.get(0, 0)