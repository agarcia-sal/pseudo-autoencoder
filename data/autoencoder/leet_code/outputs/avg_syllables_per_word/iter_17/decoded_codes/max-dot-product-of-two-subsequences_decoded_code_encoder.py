from math import inf

class Solution:
    def maxDotProduct(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        dp = self.initialize_dp_table(m + 1, n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    current_product,
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1] + current_product
                )
        return dp[m][n]

    def initialize_dp_table(self, rows, columns):
        dp = []
        for _ in range(rows):
            # Use negative infinity constant for initialization
            dp.append([self.negative_infinity_value()] * columns)
        return dp

    def negative_infinity_value(self):
        return -inf