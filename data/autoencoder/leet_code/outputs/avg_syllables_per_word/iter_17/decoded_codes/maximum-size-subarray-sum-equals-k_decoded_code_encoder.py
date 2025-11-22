class Solution:
    def maxSubArrayLen(self, list_of_numbers, target_sum):
        cumulative_sum_to_index = {0: -1}
        cumulative_sum = 0
        maximum_length = 0

        for index, current_number in enumerate(list_of_numbers):
            cumulative_sum += current_number

            if (cumulative_sum - target_sum) in cumulative_sum_to_index:
                candidate_length = index - cumulative_sum_to_index[cumulative_sum - target_sum]
                if candidate_length > maximum_length:
                    maximum_length = candidate_length

            if cumulative_sum not in cumulative_sum_to_index:
                cumulative_sum_to_index[cumulative_sum] = index

        return maximum_length