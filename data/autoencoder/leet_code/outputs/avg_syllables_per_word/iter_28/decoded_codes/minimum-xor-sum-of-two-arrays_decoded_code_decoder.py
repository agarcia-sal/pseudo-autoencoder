from typing import List
import math

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [math.inf] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            if bit_count == n:
                continue
            for j in range(n):
                bit = 1 << j
                if (mask & bit) == 0:
                    new_mask = mask | bit
                    cur = dp[mask] + (nums1[bit_count] ^ nums2[j])
                    if cur < dp[new_mask]:
                        dp[new_mask] = cur
        return dp[size - 1]