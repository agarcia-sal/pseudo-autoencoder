from bisect import bisect_right
from typing import List, Dict

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp: Dict[int, int] = {-1: 0}  # key: last_num, value: operations count

        for num in arr1:
            new_dp: Dict[int, int] = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    if num not in new_dp or new_dp[num] > ops:
                        new_dp[num] = ops

                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    candidate = arr2[idx]
                    if candidate not in new_dp or new_dp[candidate] > ops + 1:
                        new_dp[candidate] = ops + 1

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())