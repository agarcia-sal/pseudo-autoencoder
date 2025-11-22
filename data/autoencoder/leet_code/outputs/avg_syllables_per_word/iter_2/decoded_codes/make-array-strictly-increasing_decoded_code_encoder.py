from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(set(arr2))
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    if num not in new_dp or ops < new_dp[num]:
                        new_dp[num] = ops

                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replacement = arr2[idx]
                    if replacement not in new_dp or ops + 1 < new_dp[replacement]:
                        new_dp[replacement] = ops + 1

            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())