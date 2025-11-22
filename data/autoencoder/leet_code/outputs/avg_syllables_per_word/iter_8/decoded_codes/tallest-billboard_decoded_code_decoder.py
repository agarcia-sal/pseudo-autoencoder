class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                greater_key = d + rod
                new_dp[greater_key] = max(new_dp.get(greater_key, 0), y)
                difference_key = abs(d - rod)
                new_dp[difference_key] = max(new_dp.get(difference_key, 0), y + min(d, rod))
            dp = new_dp
        return dp.get(0, 0)