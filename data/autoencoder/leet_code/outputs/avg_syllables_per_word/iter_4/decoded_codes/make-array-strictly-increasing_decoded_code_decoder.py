from bisect import bisect_right
from math import inf

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    current_val = new_dp.get(num, inf)
                    new_dp[num] = min(current_val, ops)
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replace_val = arr2[idx]
                    current_val = new_dp.get(replace_val, inf)
                    new_dp[replace_val] = min(current_val, ops + 1)
            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())