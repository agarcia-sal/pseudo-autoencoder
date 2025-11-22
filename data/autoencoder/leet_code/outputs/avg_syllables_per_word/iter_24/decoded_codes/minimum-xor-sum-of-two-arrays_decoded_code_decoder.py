from math import inf

class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        size = 1 << n
        dp = [inf] * size
        dp[0] = 0
        for mask in range(size):
            bit_count = bin(mask).count("1")
            for j in range(n):
                if mask & (1 << j):
                    current_val = nums1[bit_count - 1]
                    compared_val = nums2[j]
                    xor_val = current_val ^ compared_val
                    candidate = dp[mask ^ (1 << j)] + xor_val
                    if candidate < dp[mask]:
                        dp[mask] = candidate
        return dp[size - 1]