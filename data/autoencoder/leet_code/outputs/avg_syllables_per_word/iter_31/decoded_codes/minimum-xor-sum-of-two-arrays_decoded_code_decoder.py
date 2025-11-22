from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            if bit_count == 0:
                continue

            # bit_count - 1 is the index in nums1 to use
            idx1 = bit_count - 1
            for j in range(n):
                bit = 1 << j
                if mask & bit:
                    prev_mask = mask ^ bit
                    dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[idx1] ^ nums2[j]))

        return dp[size - 1]