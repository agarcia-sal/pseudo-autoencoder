class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_for_taller_support = max(new_dp.get(d + rod, 0), y)
                new_dp[d + rod] = sum_for_taller_support

                diff = abs(d - rod)
                sum_for_shorter_support = max(new_dp.get(diff, 0), y + min(d, rod))
                new_dp[diff] = sum_for_shorter_support

            dp = new_dp
        return dp.get(0, 0)