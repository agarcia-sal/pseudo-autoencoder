from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # dp[i][0]: minimum swaps to make sequences increasing up to i without swap at i
        # dp[i][1]: minimum swaps to make sequences increasing up to i with swap at i
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, n):
            dp[i][0] = dp[i][1] = n + 1  # initialize with a large number

            # Check if both nums1 and nums2 are strictly increasing without swap at i
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                # No swap at i, and no swap at i-1
                dp[i][0] = min(dp[i][0], dp[i-1][0])
                # Swap at i, and swap at i-1
                dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)

            # Check if swapping at i makes sequences strictly increasing compared to the other array's previous element
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                # No swap at i, but swap at i-1
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                # Swap at i, but no swap at i-1
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)

        return min(dp[n-1][0], dp[n-1][1])