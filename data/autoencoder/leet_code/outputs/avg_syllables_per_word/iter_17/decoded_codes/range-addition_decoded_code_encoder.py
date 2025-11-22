class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        difference_array = [0] * (length + 1)
        for start_index, end_index, increment_value in updates:
            difference_array[start_index] += increment_value
            if end_index + 1 < length:
                difference_array[end_index + 1] -= increment_value
        result_array = [0] * length
        result_array[0] = difference_array[0]
        for i in range(1, length):
            result_array[i] = result_array[i - 1] + difference_array[i]
        return result_array