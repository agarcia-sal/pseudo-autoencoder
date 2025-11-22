from bisect import bisect_right
from math import inf

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {-1: 0}

        for number in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if number > last_num:
                    current_min = new_dp.get(number, inf)
                    new_dp[number] = min(current_min, ops)

                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replace_num = arr2[idx]
                    current_min_replace = new_dp.get(replace_num, inf)
                    new_dp[replace_num] = min(current_min_replace, ops + 1)

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())