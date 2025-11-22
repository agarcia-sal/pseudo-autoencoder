from bisect import bisect_right
from typing import List, Dict

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))  # Sort and remove duplicates for efficient searching
        dp: Dict[int, int] = {-1: 0}  # maps last number in sequence to minimum operations needed

        for num in arr1:
            new_dp: Dict[int, int] = {}
            for last_num, ops in dp.items():
                # Option 1: Keep num if it is strictly greater than last_num
                if num > last_num:
                    current_ops = new_dp.get(num, float('inf'))
                    if ops < current_ops:
                        new_dp[num] = ops

                # Option 2: Replace num with an element from arr2 that is strictly greater than last_num
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    candidate = arr2[idx]
                    current_ops = new_dp.get(candidate, float('inf'))
                    if ops + 1 < current_ops:
                        new_dp[candidate] = ops + 1

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())