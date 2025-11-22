from bisect import bisect_right
from math import inf
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    current_min_ops = new_dp.get(num, inf)
                    new_dp[num] = min(current_min_ops, ops)

                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replacement = arr2[idx]
                    current_min_ops_replace = new_dp.get(replacement, inf)
                    new_dp[replacement] = min(current_min_ops_replace, ops + 1)

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())