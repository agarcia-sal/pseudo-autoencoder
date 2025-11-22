class Solution:
    def minimumXORSum(self, nums1, nums2) -> int:
        n = len(nums1)
        size = 1 << n
        dp = [float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            bit_count = bin(mask).count('1')
            if bit_count == 0:
                continue
            current_value = nums1[bit_count - 1]
            for j in range(n):
                if (mask & (1 << j)) != 0:
                    candidate = dp[mask ^ (1 << j)] + (current_value ^ nums2[j])
                    if candidate < dp[mask]:
                        dp[mask] = candidate

        return dp[size - 1]