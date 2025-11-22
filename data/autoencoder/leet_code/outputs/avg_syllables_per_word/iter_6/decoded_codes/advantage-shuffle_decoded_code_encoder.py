class Solution:
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        nums2_with_indices = sorted(((val, i) for i, val in enumerate(nums2)), reverse=True)

        result = [0] * len(nums1)
        left, right = 0, len(nums1) - 1

        for val, i in nums2_with_indices:
            if nums1[right] > val:
                result[i] = nums1[right]
                right -= 1
            else:
                result[i] = nums1[left]
                left += 1

        return result