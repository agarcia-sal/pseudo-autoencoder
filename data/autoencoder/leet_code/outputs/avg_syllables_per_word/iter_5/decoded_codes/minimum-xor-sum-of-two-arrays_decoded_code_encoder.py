class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1, 1 << n):
            bit_count = bin(mask).count('1')
            i = bit_count - 1
            for j in range(n):
                if mask & (1 << j):
                    prev_mask = mask ^ (1 << j)
                    dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[i] ^ nums2[j]))
        return dp[(1 << n) - 1]