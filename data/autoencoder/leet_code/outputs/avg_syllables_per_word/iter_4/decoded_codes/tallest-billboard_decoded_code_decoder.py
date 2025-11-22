class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                new_dp[d + rod] = max(new_dp.get(d + rod, 0), y)
                diff = abs(d - rod)
                new_dp[diff] = max(new_dp.get(diff, 0), y + min(d, rod))
            dp = new_dp
        return dp.get(0, 0)