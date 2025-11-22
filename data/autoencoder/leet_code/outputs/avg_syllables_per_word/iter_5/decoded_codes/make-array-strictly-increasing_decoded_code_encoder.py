from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {-1: 0}
        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    if num not in new_dp or ops < new_dp[num]:
                        new_dp[num] = ops
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    if arr2[idx] not in new_dp or ops + 1 < new_dp[arr2[idx]]:
                        new_dp[arr2[idx]] = ops + 1
            if not new_dp:
                return -1
            dp = new_dp
        return min(dp.values())