class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                key1 = d + rod
                new_dp[key1] = max(new_dp.get(key1, 0), y)

                key2 = abs(d - rod)
                new_dp[key2] = max(new_dp.get(key2, 0), y + min(d, rod))
            dp = new_dp
        return dp.get(0, 0)