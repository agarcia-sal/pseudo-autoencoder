from bisect import bisect_right
from typing import Dict


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        dp: Dict[int, int] = {-1: 0}

        for num in arr1:
            new_dp: Dict[int, int] = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    new_dp[num] = min(new_dp.get(num, float('inf')), ops)
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    candidate = arr2[idx]
                    new_dp[candidate] = min(new_dp.get(candidate, float('inf')), ops + 1)
            if not new_dp:
                return -1
            dp = new_dp
        return min(dp.values())