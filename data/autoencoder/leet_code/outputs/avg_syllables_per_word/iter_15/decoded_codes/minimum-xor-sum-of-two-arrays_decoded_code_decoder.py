from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            if bit_count == 0:
                continue
            for j in range(n):
                bit = 1 << j
                if mask & bit:
                    candidate_value = dp[mask ^ bit] + (nums1[bit_count - 1] ^ nums2[j])
                    if candidate_value < dp[mask]:
                        dp[mask] = candidate_value

        return dp[(1 << n) - 1]