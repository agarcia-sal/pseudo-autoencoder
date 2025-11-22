class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            if bit_count == 0:
                continue  # no elements chosen yet, skip
            for j in range(n):
                bit = 1 << j
                if mask & bit:
                    prev_mask = mask ^ bit
                    dp[mask] = min(dp[mask], dp[prev_mask] + (nums1[bit_count - 1] ^ nums2[j]))

        return dp[(1 << n) - 1]