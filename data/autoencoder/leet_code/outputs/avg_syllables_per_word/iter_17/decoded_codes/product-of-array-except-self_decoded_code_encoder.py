from typing import List

class Solution:
    def productExceptSelf(self, list_of_numbers: List[int]) -> List[int]:
        length_of_numbers = len(list_of_numbers)
        answer_list = [1] * length_of_numbers

        left_product = 1
        for index in range(length_of_numbers):
            answer_list[index] = left_product
            left_product *= list_of_numbers[index]

        right_product = 1
        for index in range(length_of_numbers - 1, -1, -1):
            answer_list[index] *= right_product
            right_product *= list_of_numbers[index]

        return answer_list