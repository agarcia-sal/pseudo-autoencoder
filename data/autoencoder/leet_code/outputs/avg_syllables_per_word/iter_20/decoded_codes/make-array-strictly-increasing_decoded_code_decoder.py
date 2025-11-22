from bisect import bisect_right
from math import inf

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(set(arr2))
        dp = {-1: 0}
        for num in arr1:
            new_dp = dict()
            for last_num, ops in dp.items():
                if num > last_num:
                    curr_min_ops = new_dp.get(num, inf)
                    new_dp[num] = min(curr_min_ops, ops)
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replacement_num = arr2[idx]
                    curr_min_ops = new_dp.get(replacement_num, inf)
                    new_dp[replacement_num] = min(curr_min_ops, ops + 1)
            if not new_dp:
                return -1
            dp = new_dp
        return min(dp.values())