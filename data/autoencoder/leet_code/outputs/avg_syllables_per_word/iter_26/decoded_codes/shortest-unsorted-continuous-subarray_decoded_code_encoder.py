from typing import List

class Solution:
    def findUnsortedSubarray(self, list_of_numbers: List[int]) -> int:
        sorted_list = sorted(list_of_numbers)
        start_pointer = -1
        end_pointer = -2
        for index in range(len(list_of_numbers)):
            if list_of_numbers[index] != sorted_list[index]:
                if start_pointer == -1:
                    start_pointer = index
                end_pointer = index
        return end_pointer - start_pointer + 1