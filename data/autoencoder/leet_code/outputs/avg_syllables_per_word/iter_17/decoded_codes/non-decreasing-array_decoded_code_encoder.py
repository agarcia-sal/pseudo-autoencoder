from typing import List

class Solution:
    def checkPossibility(self, list_of_numbers: List[int]) -> bool:
        modified_flag = False
        for index in range(1, len(list_of_numbers)):
            if list_of_numbers[index] < list_of_numbers[index - 1]:
                if modified_flag:
                    return False
                modified_flag = True
                if index < 2 or list_of_numbers[index] >= list_of_numbers[index - 2]:
                    list_of_numbers[index - 1] = list_of_numbers[index]
                else:
                    list_of_numbers[index] = list_of_numbers[index - 1]
        return True