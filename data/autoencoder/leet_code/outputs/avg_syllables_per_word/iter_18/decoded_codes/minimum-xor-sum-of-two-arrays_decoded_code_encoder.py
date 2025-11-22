from math import inf
from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [inf] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            if bit_count == n:
                continue
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    next_mask = mask | (1 << j)
                    candidate_value = dp[mask] + (nums1[bit_count] ^ nums2[j])
                    if candidate_value < dp[next_mask]:
                        dp[next_mask] = candidate_value

        return dp[size - 1]