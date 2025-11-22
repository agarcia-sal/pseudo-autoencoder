from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_with_indices = sorted(((v, i) for i, v in enumerate(nums2)), key=lambda x: -x[0])
        result = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        for value, idx in nums2_with_indices:
            if nums1[right] > value:
                result[idx] = nums1[right]
                right -= 1
            else:
                result[idx] = nums1[left]
                left += 1
        return result