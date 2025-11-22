from bisect import bisect_right
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1: 0}  # key: last_number, value: operations

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    if num not in new_dp:
                        new_dp[num] = ops
                    else:
                        new_dp[num] = min(new_dp[num], ops)

                index = bisect_right(arr2, last_num)
                if index < len(arr2):
                    replacement = arr2[index]
                    cost = ops + 1
                    if replacement not in new_dp:
                        new_dp[replacement] = cost
                    else:
                        new_dp[replacement] = min(new_dp[replacement], cost)

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())