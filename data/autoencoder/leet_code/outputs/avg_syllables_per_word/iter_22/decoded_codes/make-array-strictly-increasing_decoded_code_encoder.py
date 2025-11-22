from bisect import bisect_right
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1: 0}  # key: last number used, value: operations count

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    current_min = new_dp.get(num, float('inf'))
                    new_dp[num] = min(current_min, ops)

                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    candidate = arr2[idx]
                    current_min_replacement = new_dp.get(candidate, float('inf'))
                    new_dp[candidate] = min(current_min_replacement, ops + 1)

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())