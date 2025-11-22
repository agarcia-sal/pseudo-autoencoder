class Solution:
    def maxSum(self, nums1, nums2):
        i, j = 0, 0
        sum1, sum2 = 0, 0
        MOD = 10**9 + 1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                maximum_value = max(sum1, sum2)
                sum1 = maximum_value + nums1[i]
                sum2 = maximum_value + nums1[i]
                i += 1
                j += 1

        while i < len(nums1):
            sum1 += nums1[i]
            i += 1

        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        result = max(sum1, sum2) % MOD
        return result