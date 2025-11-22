from typing import List

class Solution:
    def largestSumOfAverages(self, list_of_numbers: List[float], number_of_partitions: int) -> float:
        length_of_list = len(list_of_numbers)
        prefix_sum_list = [0.0] * (length_of_list + 1)
        for index in range(length_of_list):
            prefix_sum_list[index + 1] = prefix_sum_list[index] + list_of_numbers[index]

        def average(start_index: int, end_index: int) -> float:
            sum_subarray = prefix_sum_list[end_index + 1] - prefix_sum_list[start_index]
            count_subarray = end_index - start_index + 1
            return sum_subarray / count_subarray

        dp_table = [[0.0] * (number_of_partitions + 1) for _ in range(length_of_list + 1)]

        for index in range(length_of_list):
            dp_table[index][1] = average(index, length_of_list - 1)

        for index in range(length_of_list - 1, -1, -1):
            for partitions in range(2, number_of_partitions + 1):
                for split_point in range(index + 1, length_of_list):
                    candidate_value = dp_table[split_point][partitions - 1] + average(index, split_point - 1)
                    if candidate_value > dp_table[index][partitions]:
                        dp_table[index][partitions] = candidate_value

        return dp_table[0][number_of_partitions]