class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                taller = d + rod
                new_dp[taller] = max(new_dp.get(taller, 0), y)

                diff = abs(d - rod)
                new_dp[diff] = max(new_dp.get(diff, 0), y + min(d, rod))
            dp = new_dp
        return dp.get(0, 0)