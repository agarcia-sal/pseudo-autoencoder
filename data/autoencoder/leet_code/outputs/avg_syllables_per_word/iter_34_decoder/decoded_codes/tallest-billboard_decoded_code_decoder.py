class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for diff, y in dp.items():
                key = diff + rod
                new_dp[key] = max(new_dp.get(key, 0), y)

                abs_diff = abs(diff - rod)
                new_dp[abs_diff] = max(new_dp.get(abs_diff, 0), y + min(diff, rod))
            dp = new_dp
        return dp.get(0, 0)