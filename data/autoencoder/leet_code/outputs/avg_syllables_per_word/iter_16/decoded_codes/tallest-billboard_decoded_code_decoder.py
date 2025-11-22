class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                key_for_taller_support = d + rod
                value_for_taller_support = max(new_dp.get(key_for_taller_support, 0), y)
                new_dp[key_for_taller_support] = value_for_taller_support

                if d - rod >= 0:
                    difference = d - rod
                    minimum_support = rod
                else:
                    difference = rod - d
                    minimum_support = d

                key_for_shorter_support = difference
                value_for_shorter_support = max(new_dp.get(key_for_shorter_support, 0), y + minimum_support)
                new_dp[key_for_shorter_support] = value_for_shorter_support
            dp = new_dp
        return dp.get(0, 0)