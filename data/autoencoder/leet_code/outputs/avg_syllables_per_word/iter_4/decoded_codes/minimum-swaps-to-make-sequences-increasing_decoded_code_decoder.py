from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1])
                    dp[i][1] = dp[i][0] + 1
                else:
                    dp[i][0] = dp[i - 1][0]
                    dp[i][1] = dp[i - 1][1] + 1
            else:
                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                    dp[i][0] = dp[i - 1][1]
                    dp[i][1] = dp[i - 1][0] + 1
                else:
                    dp[i][0] = dp[i - 1][1]
                    dp[i][1] = dp[i - 1][0] + 1

        return min(dp[n - 1][0], dp[n - 1][1])