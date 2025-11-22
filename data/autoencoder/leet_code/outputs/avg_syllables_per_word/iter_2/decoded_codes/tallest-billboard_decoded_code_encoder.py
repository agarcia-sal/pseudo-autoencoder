from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum1 = new_dp.get(d + rod, 0)
                new_dp[d + rod] = max(sum1, y)

                difference = abs(d - rod)
                sum2 = new_dp.get(difference, 0)
                new_dp[difference] = max(sum2, y + min(d, rod))
            dp = new_dp

        return dp.get(0, 0)