from math import inf
from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [inf] * (1 << n)
        dp[0] = 0
        for mask in range(1, 1 << n):
            bit_count = bin(mask).count('1')
            i = bit_count - 1
            # Try all j where the j-th bit is set in mask
            submask = mask
            while submask:
                # Extract the rightmost set bit
                rightmost = submask & -submask
                j = rightmost.bit_length() - 1
                prev_mask = mask ^ (1 << j)
                dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[i] ^ nums2[j]))
                submask ^= rightmost
        return dp[(1 << n) - 1]