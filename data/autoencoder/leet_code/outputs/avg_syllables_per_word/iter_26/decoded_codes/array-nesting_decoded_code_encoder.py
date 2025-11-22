from typing import List

class Solution:
    def arrayNesting(self, list_of_numbers: List[int]) -> int:
        visited_list = [False] * len(list_of_numbers)
        maximum_length = 0

        for index in range(len(list_of_numbers)):
            if not visited_list[index]:
                current_length = 0
                current_position = index
                while not visited_list[current_position]:
                    visited_list[current_position] = True
                    current_position = list_of_numbers[current_position]
                    current_length += 1
                maximum_length = max(maximum_length, current_length)

        return maximum_length