from typing import List

class Solution:
    def sortColors(self, list_of_numbers: List[int]) -> None:
        low, mid, high = 0, 0, len(list_of_numbers) - 1

        while mid <= high:
            if list_of_numbers[mid] == 0:
                list_of_numbers[low], list_of_numbers[mid] = list_of_numbers[mid], list_of_numbers[low]
                low += 1
                mid += 1
            elif list_of_numbers[mid] == 1:
                mid += 1
            else:
                list_of_numbers[mid], list_of_numbers[high] = list_of_numbers[high], list_of_numbers[mid]
                high -= 1