from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            if bit_count == n:
                continue
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    next_mask = mask | (1 << j)
                    dp[next_mask] = min(dp[next_mask], dp[mask] + (nums1[bit_count] ^ nums2[j]))

        return dp[size - 1]