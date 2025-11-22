from typing import List

class Solution:
    def search(self, list_of_numbers: List[int], target_value: int) -> bool:
        if not list_of_numbers:
            return False

        left_index, right_index = 0, len(list_of_numbers) - 1

        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2

            if list_of_numbers[middle_index] == target_value:
                return True

            if (list_of_numbers[left_index] == list_of_numbers[middle_index] == list_of_numbers[right_index]):
                left_index += 1
                right_index -= 1
            elif list_of_numbers[left_index] <= list_of_numbers[middle_index]:
                if list_of_numbers[left_index] <= target_value < list_of_numbers[middle_index]:
                    right_index = middle_index - 1
                else:
                    left_index = middle_index + 1
            else:
                if list_of_numbers[middle_index] < target_value <= list_of_numbers[right_index]:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index - 1

        return False