from collections import defaultdict
from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}  # key: difference between two sides, value: max sum of shorter side
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                # Option 1: add rod to the taller side
                sum_taller = d + rod
                if new_dp.get(sum_taller, 0) < y:
                    new_dp[sum_taller] = y

                # Option 2: add rod to the shorter side
                difference = abs(d - rod)
                sum_shorter_candidate = y + min(d, rod)
                if new_dp.get(difference, 0) < sum_shorter_candidate:
                    new_dp[difference] = sum_shorter_candidate
            dp = new_dp
        return dp.get(0, 0)