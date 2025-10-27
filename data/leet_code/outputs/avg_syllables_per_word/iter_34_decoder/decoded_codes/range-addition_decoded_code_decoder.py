from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        difference_array = [0] * (length + 1)
        for update in updates:
            start_index, end_index, increment_value = update
            difference_array[start_index] += increment_value
            if end_index + 1 < length:
                difference_array[end_index + 1] -= increment_value

        result_array = [0] * length
        if length > 0:
            result_array[0] = difference_array[0]
            for index in range(1, length):
                result_array[index] = result_array[index - 1] + difference_array[index]

        return result_array