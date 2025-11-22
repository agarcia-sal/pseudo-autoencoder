from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            for j in range(n):
                bit = 1 << j
                if mask & bit:
                    prev_mask = mask ^ bit
                    cost = dp[prev_mask] + (nums1[bit_count - 1] ^ nums2[j])
                    if cost < dp[mask]:
                        dp[mask] = cost

        return dp[size - 1]