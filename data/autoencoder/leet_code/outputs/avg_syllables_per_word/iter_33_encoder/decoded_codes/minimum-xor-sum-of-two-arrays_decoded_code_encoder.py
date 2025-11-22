class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        size = 1 << n
        dp = [float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            for j in range(n):
                if (mask & (1 << j)) != 0:
                    prev_mask = mask ^ (1 << j)
                    dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[bit_count - 1] ^ nums2[j]))

        return dp[size - 1]