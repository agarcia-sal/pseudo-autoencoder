from bisect import bisect_right
from math import inf
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    new_dp[num] = min(new_dp.get(num, inf), ops)
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    new_dp[arr2[idx]] = min(new_dp.get(arr2[idx], inf), ops + 1)
            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())