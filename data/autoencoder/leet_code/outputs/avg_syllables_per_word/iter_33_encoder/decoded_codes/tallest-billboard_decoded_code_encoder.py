class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                sum_for_taller_support = d + rod
                if sum_for_taller_support in new_dp:
                    new_dp[sum_for_taller_support] = max(new_dp[sum_for_taller_support], y)
                else:
                    new_dp[sum_for_taller_support] = y

                difference = abs(d - rod)
                candidate_value = y + min(d, rod)
                if difference in new_dp:
                    new_dp[difference] = max(new_dp[difference], candidate_value)
                else:
                    new_dp[difference] = candidate_value
            dp = new_dp
        return dp.get(0, 0)