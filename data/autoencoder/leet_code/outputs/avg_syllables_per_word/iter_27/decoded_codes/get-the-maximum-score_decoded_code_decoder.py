from typing import List

class Solution:
    def maxSum(self, nums1_list: List[int], nums2_list: List[int]) -> int:
        i = 0
        j = 0
        sum1 = 0
        sum2 = 0
        MOD = 10**9 + 1

        while i < len(nums1_list) and j < len(nums2_list):
            if nums1_list[i] < nums2_list[j]:
                sum1 += nums1_list[i]
                i += 1
            elif nums1_list[i] > nums2_list[j]:
                sum2 += nums2_list[j]
                j += 1
            else:
                sum1 = max(sum1, sum2) + nums1_list[i]
                sum2 = sum1
                i += 1
                j += 1

        while i < len(nums1_list):
            sum1 += nums1_list[i]
            i += 1

        while j < len(nums2_list):
            sum2 += nums2_list[j]
            j += 1

        return max(sum1, sum2) % MOD