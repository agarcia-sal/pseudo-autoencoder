from typing import List

class Solution:
    def getModifiedArray(self, length_parameter: int, updates_parameter: List[List[int]]) -> List[int]:
        diff_array = [0] * (length_parameter + 1)
        for start_index_element, end_index_element, increment_element in updates_parameter:
            diff_array[start_index_element] += increment_element
            if start_index_element + 1 <= end_index_element:
                if end_index_element + 1 < length_parameter:
                    diff_array[end_index_element + 1] -= increment_element

        result_array = [0] * length_parameter
        if length_parameter > 0:
            result_array[0] = diff_array[0]
        for index_variable in range(1, length_parameter):
            result_array[index_variable] = result_array[index_variable - 1] + diff_array[index_variable]

        return result_array