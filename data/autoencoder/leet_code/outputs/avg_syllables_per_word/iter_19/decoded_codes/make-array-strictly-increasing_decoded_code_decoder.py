from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {-1: 0}  # key: last number in sequence, value: operations count

        for num in arr1:
            new_dp = {}
            for last_num, ops in dp.items():
                if num > last_num:
                    if num not in new_dp or new_dp[num] > ops:
                        new_dp[num] = ops
                index = bisect_right(arr2, last_num)
                if index < len(arr2):
                    candidate_num = arr2[index]
                    candidate_ops = ops + 1
                    if candidate_num not in new_dp or new_dp[candidate_num] > candidate_ops:
                        new_dp[candidate_num] = candidate_ops
            if not new_dp:
                return -1
            dp = new_dp

        return min(dp.values())