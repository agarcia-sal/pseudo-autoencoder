class Solution:
    def minTaps(self, number_n: int, list_ranges: list[int]) -> int:
        list_max_range = [0] * (number_n + 1)

        for index_i in range(number_n + 1):
            if list_ranges[index_i] > 0:
                value_left = max(0, index_i - list_ranges[index_i])
                value_right = min(number_n, index_i + list_ranges[index_i])
                list_max_range[value_left] = max(list_max_range[value_left], value_right)

        variable_taps = 0
        variable_current_end = 0
        variable_farthest = 0

        for index_i in range(number_n + 1):
            if index_i > variable_farthest:
                return -1
            if index_i > variable_current_end:
                variable_taps += 1
                variable_current_end = variable_farthest
            variable_farthest = max(variable_farthest, list_max_range[index_i])

        return variable_taps