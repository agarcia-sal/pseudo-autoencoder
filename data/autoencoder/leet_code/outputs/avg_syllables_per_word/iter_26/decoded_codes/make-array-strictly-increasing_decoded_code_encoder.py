from bisect import bisect_right
from math import inf

class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        dp = {-1: 0}  # Dictionary mapping last number to min operations

        for number in arr1:
            new_dp = {}
            for last_number, operations in dp.items():
                if number > last_number:
                    if number not in new_dp:
                        new_dp[number] = inf
                    new_dp[number] = min(new_dp[number], operations)

                index = bisect_right(arr2, last_number)
                if index < len(arr2):
                    replaced = arr2[index]
                    if replaced not in new_dp:
                        new_dp[replaced] = inf
                    new_dp[replaced] = min(new_dp[replaced], operations + 1)

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())