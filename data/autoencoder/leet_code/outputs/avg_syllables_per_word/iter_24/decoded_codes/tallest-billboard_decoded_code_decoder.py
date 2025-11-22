from typing import List, Dict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp: Dict[int, int] = {0: 0}
        for rod in rods:
            new_dp = dict(dp)
            for d, y in dp.items():
                new_key_one = d + rod
                if new_key_one in new_dp:
                    if new_dp[new_key_one] < y:
                        new_dp[new_key_one] = y
                else:
                    new_dp[new_key_one] = y

                difference = abs(d - rod)
                minimum_value = d if d < rod else rod
                new_value_two = y + minimum_value
                if difference in new_dp:
                    if new_dp[difference] < new_value_two:
                        new_dp[difference] = new_value_two
                else:
                    new_dp[difference] = new_value_two
            dp = new_dp
        return dp.get(0, 0)