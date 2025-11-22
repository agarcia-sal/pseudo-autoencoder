import bisect
import math

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    current_min = new_dp.get(num, math.inf)
                    new_dp[num] = min(current_min, ops)

                idx = bisect.bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replacement_num = arr2[idx]
                    current_min_replacement = new_dp.get(replacement_num, math.inf)
                    new_dp[replacement_num] = min(current_min_replacement, ops + 1)

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())