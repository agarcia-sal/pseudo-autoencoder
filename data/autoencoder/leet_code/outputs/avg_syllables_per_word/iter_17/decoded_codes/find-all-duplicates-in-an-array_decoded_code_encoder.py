from typing import List

class Solution:
    def findDuplicates(self, list_of_numbers: List[int]) -> List[int]:
        for index in range(len(list_of_numbers)):
            while list_of_numbers[index] != list_of_numbers[list_of_numbers[index] - 1]:
                temp = list_of_numbers[index]
                list_of_numbers[index], list_of_numbers[temp - 1] = list_of_numbers[temp - 1], list_of_numbers[index]
        return [value for index_value, value in enumerate(list_of_numbers) if value != index_value + 1]