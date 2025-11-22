from typing import List

class Solution:
    def isIdealPermutation(self, list_of_numbers: List[int]) -> bool:
        for index in range(len(list_of_numbers)):
            if abs(list_of_numbers[index] - index) > 1:
                return False
        return True