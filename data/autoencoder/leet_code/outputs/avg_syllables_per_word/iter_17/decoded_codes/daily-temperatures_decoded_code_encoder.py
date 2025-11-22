from typing import List

class Solution:
    def dailyTemperatures(self, list_of_temperatures: List[int]) -> List[int]:
        length_of_temperatures = len(list_of_temperatures)
        answer_list = [0] * length_of_temperatures
        stack_list = []

        for index in range(length_of_temperatures):
            while stack_list and list_of_temperatures[index] > list_of_temperatures[stack_list[-1]]:
                previous_index = stack_list.pop()
                answer_list[previous_index] = index - previous_index
            stack_list.append(index)

        return answer_list