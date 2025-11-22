class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                key_for_taller_support = d + rod
                current_value_for_taller_support = new_dp.get(key_for_taller_support, 0)
                value_for_taller_support = max(current_value_for_taller_support, y)
                new_dp[key_for_taller_support] = value_for_taller_support

                difference = abs(d - rod)
                current_value_for_shorter_support = new_dp.get(difference, 0)
                smaller_height = min(d, rod)
                value_for_shorter_support = max(current_value_for_shorter_support, y + smaller_height)
                new_dp[difference] = value_for_shorter_support
            dp = new_dp
        return dp.get(0, 0)