from typing import List

def CREATE_TWO_DIMENSIONAL_LIST(row_count: int, column_count: int) -> List[List[int]]:
    return [[0] * column_count for _ in range(row_count)]

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = CREATE_TWO_DIMENSIONAL_LIST(len(nums1) + 1, len(nums2) + 1)
        max_length = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
        return max_length