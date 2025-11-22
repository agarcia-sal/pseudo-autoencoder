class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                sum1 = max(new_dp.get(d + rod, 0), y)
                new_dp[d + rod] = sum1
                abs_diff = abs(d - rod)
                sum2 = max(new_dp.get(abs_diff, 0), y + min(d, rod))
                new_dp[abs_diff] = sum2
            dp = new_dp
        return dp.get(0, 0)