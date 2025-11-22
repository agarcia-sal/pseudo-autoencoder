class Solution:
    def minimumXORSum(self, nums1, nums2) -> int:
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            for j in range(n):
                bit = 1 << j
                if mask & bit:
                    prev_mask = mask ^ bit
                    val = dp[prev_mask] + (nums1[bit_count - 1] ^ nums2[j])
                    if val < dp[mask]:
                        dp[mask] = val
        return dp[(1 << n) - 1]