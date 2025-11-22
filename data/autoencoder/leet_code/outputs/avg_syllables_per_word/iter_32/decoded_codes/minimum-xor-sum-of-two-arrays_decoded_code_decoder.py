from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # dp[mask]: minimum XOR sum for subset represented by mask
        # mask bits represent which elements in nums2 have been used
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            if bit_count > n:
                continue  # just a safe guard, not really needed because mask fits n bits
            # The bit_count-th element in nums1 is to be matched now (0-based: bit_count-1 for the XOR)
            # but they use bit_count - 1 in XOR, so when bit_count=0, no elements matched (so skip)
            if bit_count == 0:
                continue

            i = bit_count - 1  # index in nums1
            for j in range(n):
                # if j-th bit in mask is set, try using nums2[j]
                if (mask & (1 << j)):
                    prev_mask = mask ^ (1 << j)
                    dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[i] ^ nums2[j]))

        return dp[(1 << n) - 1]