from typing import List, Tuple

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        # Create pairs of (index, value) for nums2
        nums2_with_indices: List[Tuple[int, int]] = list(enumerate(nums2))
        # Sort pairs of nums2 in descending order by value
        sorted_nums2_with_indices = sorted(nums2_with_indices, key=lambda x: x[1], reverse=True)
        result = [0] * len(nums1)
        left, right = 0, len(nums1) - 1

        for index, value in sorted_nums2_with_indices:
            if nums1[right] > value:
                result[index] = nums1[right]
                right -= 1
            else:
                result[index] = nums1[left]
                left += 1

        return result