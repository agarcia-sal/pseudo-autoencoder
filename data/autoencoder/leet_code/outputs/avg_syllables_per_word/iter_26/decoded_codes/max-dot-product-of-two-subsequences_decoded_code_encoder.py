class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        # Initialize dp with very small numbers to represent minimum possible values
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_product = nums1[i - 1] * nums2[j - 1]
                candidate_1 = current_product
                candidate_2 = dp[i - 1][j]
                candidate_3 = dp[i][j - 1]
                candidate_4 = dp[i - 1][j - 1] + current_product
                dp[i][j] = max(candidate_1, candidate_2, candidate_3, candidate_4)

        return dp[m][n]