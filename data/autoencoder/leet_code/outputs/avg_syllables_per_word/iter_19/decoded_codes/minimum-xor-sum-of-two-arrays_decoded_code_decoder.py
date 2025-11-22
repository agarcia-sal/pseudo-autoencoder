from math import inf

class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        size = 1 << n
        dp = [inf] * size
        dp[0] = 0
        for mask in range(size):
            bit_count = bin(mask).count("1")
            if bit_count == 0:
                continue
            for j in range(n):
                bit = 1 << j
                if mask & bit:
                    prev_mask = mask ^ bit
                    candidate_value = dp[prev_mask] + (nums1[bit_count - 1] ^ nums2[j])
                    if candidate_value < dp[mask]:
                        dp[mask] = candidate_value
        return dp[size - 1]