class Solution:
    def maxDotProduct(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        dp = self.initializeTwoDimensionalList(m + 1, n + 1, float('-inf'))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_product = nums1[i - 1] * nums2[j - 1]

                candidate_one = current_product
                candidate_two = dp[i - 1][j]
                candidate_three = dp[i][j - 1]
                candidate_four = dp[i - 1][j - 1] + current_product

                dp[i][j] = max(candidate_one, candidate_two, candidate_three, candidate_four)

        return dp[m][n]

    def initializeTwoDimensionalList(self, rows, cols, initial_value):
        table = []
        for _ in range(rows):
            current_row = [initial_value] * cols
            table.append(current_row)
        return table