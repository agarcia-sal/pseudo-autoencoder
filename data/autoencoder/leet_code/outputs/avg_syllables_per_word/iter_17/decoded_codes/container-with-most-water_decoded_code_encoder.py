from typing import List

class Solution:
    def maxArea(self, height_list: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height_list) - 1
        maximum_area = 0

        while left_pointer < right_pointer:
            current_area = min(height_list[left_pointer], height_list[right_pointer]) * (right_pointer - left_pointer)
            if current_area > maximum_area:
                maximum_area = current_area

            if height_list[left_pointer] < height_list[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return maximum_area