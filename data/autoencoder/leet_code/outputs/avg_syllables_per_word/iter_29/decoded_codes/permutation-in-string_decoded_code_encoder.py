from collections import Counter

class Solution:
    def checkInclusion(self, string_parameter_one: str, string_parameter_two: str) -> bool:
        length_of_string_one = len(string_parameter_one)
        length_of_string_two = len(string_parameter_two)

        if length_of_string_one > length_of_string_two:
            return False

        frequency_count_of_string_one = Counter(string_parameter_one)
        frequency_count_of_first_window_of_string_two = Counter(string_parameter_two[:length_of_string_one])

        if frequency_count_of_string_one == frequency_count_of_first_window_of_string_two:
            return True

        for index in range(length_of_string_one, length_of_string_two):
            entering_char = string_parameter_two[index]
            leaving_char = string_parameter_two[index - length_of_string_one]

            frequency_count_of_first_window_of_string_two[entering_char] += 1
            frequency_count_of_first_window_of_string_two[leaving_char] -= 1

            if frequency_count_of_first_window_of_string_two[leaving_char] == 0:
                del frequency_count_of_first_window_of_string_two[leaving_char]

            if frequency_count_of_string_one == frequency_count_of_first_window_of_string_two:
                return True

        return False