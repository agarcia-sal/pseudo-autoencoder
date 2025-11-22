from collections import Counter
from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MODULO = 10**9 + 7
        maximum_number = max(nums)
        count_map = Counter(nums)
        prefix_sum_list = [0] * (maximum_number + 1)

        for number in count_map:
            prefix_sum_list[number] += count_map[number]

        for index in range(1, maximum_number + 1):
            prefix_sum_list[index] += prefix_sum_list[index - 1]

        result_sum = 0

        for number in count_map:
            count_num = count_map[number]
            max_multiplier = maximum_number // number
            for multiplier in range(1, max_multiplier + 1):
                start_position = number * multiplier
                end_position = min(number * (multiplier + 1) - 1, maximum_number)
                multiples_count = prefix_sum_list[end_position] - prefix_sum_list[start_position - 1]
                increment_value = multiples_count * multiplier * count_num
                result_sum = (result_sum + increment_value) % MODULO

        return result_sum