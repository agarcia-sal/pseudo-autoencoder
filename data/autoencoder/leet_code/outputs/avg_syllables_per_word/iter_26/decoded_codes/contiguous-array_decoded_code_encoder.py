class Solution:
    def findMaxLength(self, list_of_numbers):
        prefix_sum_positions = {0: -1}
        maximum_length = 0
        count_tracker = 0

        for index_number, element_value in enumerate(list_of_numbers):
            if element_value == 1:
                count_tracker += 1
            else:
                count_tracker -= 1

            if count_tracker in prefix_sum_positions:
                maximum_length = max(maximum_length, index_number - prefix_sum_positions[count_tracker])
            else:
                prefix_sum_positions[count_tracker] = index_number

        return maximum_length