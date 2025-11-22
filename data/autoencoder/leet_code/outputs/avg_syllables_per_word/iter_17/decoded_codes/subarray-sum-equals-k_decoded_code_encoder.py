from collections import defaultdict

class Solution:
    def subarraySum(self, list_of_numbers, target_value):
        cumulative_sum_frequency = defaultdict(int)
        cumulative_sum_frequency[0] = 1
        current_cumulative_sum = 0
        subarray_count = 0

        for number in list_of_numbers:
            current_cumulative_sum += number
            diff = current_cumulative_sum - target_value
            if diff in cumulative_sum_frequency:
                subarray_count += cumulative_sum_frequency[diff]
            cumulative_sum_frequency[current_cumulative_sum] += 1

        return subarray_count