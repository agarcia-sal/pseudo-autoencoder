class Solution:
    def subarraySum(self, list_of_numbers, target_value):
        cumulative_sum_frequency = {0: 1}
        current_cumulative_sum = 0
        count_of_subarrays = 0

        for number in list_of_numbers:
            current_cumulative_sum += number
            diff = current_cumulative_sum - target_value
            if diff in cumulative_sum_frequency:
                count_of_subarrays += cumulative_sum_frequency[diff]
            cumulative_sum_frequency[current_cumulative_sum] = cumulative_sum_frequency.get(current_cumulative_sum, 0) + 1

        return count_of_subarrays