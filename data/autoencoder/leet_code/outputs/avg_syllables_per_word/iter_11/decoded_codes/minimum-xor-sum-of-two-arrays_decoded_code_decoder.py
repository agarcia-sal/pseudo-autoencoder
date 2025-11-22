from math import inf

class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        dp = [inf] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            for j in range(n):
                if mask & (1 << j):
                    dp[mask] = min(dp[mask], dp[mask ^ (1 << j)] + (nums1[bit_count - 1] ^ nums2[j]))

        return dp[(1 << n) - 1]