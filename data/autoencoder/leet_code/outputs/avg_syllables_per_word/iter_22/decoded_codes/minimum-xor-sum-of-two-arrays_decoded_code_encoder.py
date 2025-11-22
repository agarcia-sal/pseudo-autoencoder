from math import inf

class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [inf] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            for j in range(n):
                bit = 1 << j
                if mask & bit == 0:
                    candidate = dp[mask ^ bit] + (nums1[bit_count] ^ nums2[j])
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        return dp[size - 1]