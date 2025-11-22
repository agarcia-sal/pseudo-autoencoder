from math import inf

class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        size = 1 << n
        dp = [inf] * size
        dp[0] = 0
        for mask in range(size):
            bit_count = bin(mask).count('1')
            for j in range(n):
                if (mask >> j) & 1:
                    previous_mask = mask ^ (1 << j)
                    xor_value = nums1[bit_count - 1] ^ nums2[j]
                    dp[mask] = min(dp[mask], dp[previous_mask] + xor_value)
        return dp[size - 1]