from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0, 0] for _ in range(n)]  # dp[i][0]: min swaps if no swap at i; dp[i][1]: min swaps if swap at i
        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, n):
            no_swap_cond = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            cross_swap_cond = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]

            if no_swap_cond:
                if cross_swap_cond:
                    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1])
                    dp[i][1] = dp[i][0] + 1
                else:
                    dp[i][0] = dp[i - 1][0]
                    dp[i][1] = dp[i - 1][1] + 1
            else:
                if cross_swap_cond:
                    dp[i][0] = dp[i - 1][1]
                    dp[i][1] = dp[i - 1][0] + 1
                else:
                    dp[i][0] = dp[i - 1][1]
                    dp[i][1] = dp[i - 1][0] + 1

        return min(dp[n - 1][0], dp[n - 1][1])