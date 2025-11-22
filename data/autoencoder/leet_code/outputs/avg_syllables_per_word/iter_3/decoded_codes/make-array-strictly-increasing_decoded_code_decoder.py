from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {-1: 0}

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    curr_min = new_dp.get(num, float('inf'))
                    new_dp[num] = min(curr_min, ops)
                idx = bisect_right(arr2, last_num)
                if idx < len(arr2):
                    replacement = arr2[idx]
                    curr_min = new_dp.get(replacement, float('inf'))
                    new_dp[replacement] = min(curr_min, ops + 1)
            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())