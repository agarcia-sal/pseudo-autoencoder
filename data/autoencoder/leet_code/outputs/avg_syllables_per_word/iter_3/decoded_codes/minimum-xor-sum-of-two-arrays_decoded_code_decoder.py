class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        size = 1 << n
        dp = [float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            if bit_count == 0:
                continue
            i = bit_count - 1
            for j in range(n):
                if mask & (1 << j):
                    prev_mask = mask ^ (1 << j)
                    dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[i] ^ nums2[j]))
        return dp[size - 1]