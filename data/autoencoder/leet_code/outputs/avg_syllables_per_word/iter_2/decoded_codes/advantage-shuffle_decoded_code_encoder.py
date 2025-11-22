from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_with_indices = sorted([(v, i) for i, v in enumerate(nums2)], reverse=True)

        result = [0] * len(nums1)
        left, right = 0, len(nums1) - 1

        for value, index in nums2_with_indices:
            if nums1[right] > value:
                result[index] = nums1[right]
                right -= 1
            else:
                result[index] = nums1[left]
                left += 1

        return result