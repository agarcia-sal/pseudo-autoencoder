class Solution:
    def hIndex(self, list_of_citations: list[int]) -> int:
        total_number = len(list_of_citations)
        left_pointer, right_pointer = 0, total_number - 1
        current_h_index = 0

        while left_pointer <= right_pointer:
            middle_position = left_pointer + (right_pointer - left_pointer) // 2
            if list_of_citations[middle_position] >= total_number - middle_position:
                current_h_index = total_number - middle_position
                right_pointer = middle_position - 1
            else:
                left_pointer = middle_position + 1

        return current_h_index