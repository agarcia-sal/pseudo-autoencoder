from bisect import bisect_right
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1: 0}
        for number in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if number > last_num:
                    if number not in new_dp or new_dp[number] > ops:
                        new_dp[number] = ops
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replacement = arr2[idx]
                    if replacement not in new_dp or new_dp[replacement] > ops + 1:
                        new_dp[replacement] = ops + 1
            if not new_dp:
                return -1
            dp = new_dp
        return min(dp.values())