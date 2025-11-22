class Solution:
    def getModifiedArray(self, length, updates):
        difference_array = [0] * (length + 1)

        for update_triplet in updates:
            start_index = update_triplet[0]
            end_index = update_triplet[1]
            increment_value = update_triplet[2]
            difference_array[start_index] += increment_value

            if end_index + 1 < length:
                difference_array[end_index + 1] -= increment_value

        result_array = [0] * length
        result_array[0] = difference_array[0]

        for index in range(1, length):
            result_array[index] = result_array[index - 1] + difference_array[index]

        return result_array