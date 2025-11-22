from typing import List

class Solution:
    def searchRange(self, list_of_numbers: List[int], target_value: int) -> List[int]:
        def find_left(nums: List[int], target: int) -> int:
            left_pointer, right_pointer = 0, len(nums) - 1
            while left_pointer <= right_pointer:
                middle_index = (left_pointer + right_pointer) // 2
                if nums[middle_index] < target:
                    left_pointer = middle_index + 1
                else:
                    right_pointer = middle_index - 1
            return left_pointer

        def find_right(nums: List[int], target: int) -> int:
            left_pointer, right_pointer = 0, len(nums) - 1
            while left_pointer <= right_pointer:
                middle_index = (left_pointer + right_pointer) // 2
                if nums[middle_index] <= target:
                    left_pointer = middle_index + 1
                else:
                    right_pointer = middle_index - 1
            return right_pointer

        left_index = find_left(list_of_numbers, target_value)
        right_index = find_right(list_of_numbers, target_value)

        if (
            left_index <= right_index
            and 0 <= right_index < len(list_of_numbers)
            and list_of_numbers[left_index] == target_value
        ):
            return [left_index, right_index]
        else:
            return [-1, -1]