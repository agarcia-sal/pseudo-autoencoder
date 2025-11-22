class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                # Option 1: add rod to the taller support
                key_for_taller_support = d + rod
                if key_for_taller_support not in new_dp or new_dp[key_for_taller_support] < y:
                    new_dp[key_for_taller_support] = y

                # Option 2: add rod to the shorter support
                absolute_difference = abs(d - rod)
                candidate_value = y + min(d, rod)
                if absolute_difference not in new_dp or new_dp[absolute_difference] < candidate_value:
                    new_dp[absolute_difference] = candidate_value
            dp = new_dp
        return dp.get(0, 0)