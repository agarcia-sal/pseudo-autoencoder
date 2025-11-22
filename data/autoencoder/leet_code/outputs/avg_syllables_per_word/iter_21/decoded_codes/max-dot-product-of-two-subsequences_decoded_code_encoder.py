from math import inf
from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = self.initializeDPTable(m, n)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_product = nums1[i - 1] * nums2[j - 1]

                candidate_one = current_product
                candidate_two = dp[i - 1][j]
                candidate_three = dp[i][j - 1]
                candidate_four = dp[i - 1][j - 1] + current_product

                dp[i][j] = max(candidate_one, candidate_two, candidate_three, candidate_four)

        return dp[m][n]

    def initializeDPTable(self, m: int, n: int) -> List[List[int]]:
        neg_inf = -inf
        dp = []
        for _ in range(m + 1):
            row = [neg_inf] * (n + 1)
            dp.append(row)
        return dp