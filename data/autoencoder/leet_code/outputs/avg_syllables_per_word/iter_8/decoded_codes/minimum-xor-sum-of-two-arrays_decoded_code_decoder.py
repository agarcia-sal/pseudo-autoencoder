class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            bit_count = bin(mask).count('1')
            for j in range(n):
                if (mask >> j) & 1:
                    previous_mask = mask ^ (1 << j)
                    candidate_value = dp[previous_mask] + (nums1[bit_count - 1] ^ nums2[j])
                    if candidate_value < dp[mask]:
                        dp[mask] = candidate_value
        return dp[(1 << n) - 1]