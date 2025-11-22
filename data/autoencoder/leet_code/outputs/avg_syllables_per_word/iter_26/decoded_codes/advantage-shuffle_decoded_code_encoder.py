from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        list_of_pairs = sorted(((val, idx) for idx, val in enumerate(nums2)), reverse=True, key=lambda x: x[0])

        result_list = [0] * len(nums1)
        left_pointer, right_pointer = 0, len(nums1) - 1

        for current_value, current_index in list_of_pairs:
            if nums1[right_pointer] > current_value:
                result_list[current_index] = nums1[right_pointer]
                right_pointer -= 1
            else:
                result_list[current_index] = nums1[left_pointer]
                left_pointer += 1

        return result_list