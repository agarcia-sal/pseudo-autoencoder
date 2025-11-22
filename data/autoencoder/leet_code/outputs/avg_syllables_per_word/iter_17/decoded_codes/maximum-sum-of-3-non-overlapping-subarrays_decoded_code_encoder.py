from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, list_of_numbers: List[int], subarray_length: int) -> List[int]:
        total_numbers = len(list_of_numbers)
        list_of_subarray_sums = [0] * (total_numbers - subarray_length + 1)

        current_sum = sum(list_of_numbers[:subarray_length])
        list_of_subarray_sums[0] = current_sum
        for index in range(1, total_numbers - subarray_length + 1):
            current_sum += list_of_numbers[index + subarray_length - 1] - list_of_numbers[index - 1]
            list_of_subarray_sums[index] = current_sum

        left_max_indices = [0] * (total_numbers - subarray_length + 1)
        right_max_indices = [total_numbers - subarray_length] * (total_numbers - subarray_length + 1)

        max_sum_index = 0
        for index in range(total_numbers - subarray_length + 1):
            if list_of_subarray_sums[index] > list_of_subarray_sums[max_sum_index]:
                max_sum_index = index
            left_max_indices[index] = max_sum_index

        max_sum_index = total_numbers - subarray_length
        for index in range(total_numbers - subarray_length, -1, -1):
            if list_of_subarray_sums[index] >= list_of_subarray_sums[max_sum_index]:
                max_sum_index = index
            right_max_indices[index] = max_sum_index

        max_total_sum = 0
        result_indices = [0, 0, 0]

        for middle_index in range(subarray_length, total_numbers - 2 * subarray_length + 1):
            left_index = left_max_indices[middle_index - subarray_length]
            right_index = right_max_indices[middle_index + subarray_length]
            total_sum = (list_of_subarray_sums[left_index] + 
                         list_of_subarray_sums[middle_index] + 
                         list_of_subarray_sums[right_index])
            if total_sum > max_total_sum:
                max_total_sum = total_sum
                result_indices = [left_index, middle_index, right_index]

        return result_indices