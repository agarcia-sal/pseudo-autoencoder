class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                key_for_taller = d + rod
                if key_for_taller not in new_dp or new_dp[key_for_taller] < y:
                    new_dp[key_for_taller] = y
                difference = abs(d - rod)
                sum_shorter = y + min(d, rod)
                if difference not in new_dp or new_dp[difference] < sum_shorter:
                    new_dp[difference] = sum_shorter
            dp = new_dp
        return dp.get(0, 0)