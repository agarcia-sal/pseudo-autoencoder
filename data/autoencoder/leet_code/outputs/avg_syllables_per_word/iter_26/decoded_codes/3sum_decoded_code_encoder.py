from typing import List

class Solution:
    def threeSum(self, list_of_numbers: List[int]) -> List[List[int]]:
        list_of_numbers.sort()
        result_list = []
        length_of_numbers = len(list_of_numbers)

        for i in range(length_of_numbers - 2):
            if i > 0 and list_of_numbers[i] == list_of_numbers[i - 1]:
                continue

            left_pointer = i + 1
            right_pointer = length_of_numbers - 1

            while left_pointer < right_pointer:
                total_sum = list_of_numbers[i] + list_of_numbers[left_pointer] + list_of_numbers[right_pointer]

                if total_sum == 0:
                    result_list.append([list_of_numbers[i], list_of_numbers[left_pointer], list_of_numbers[right_pointer]])

                    while left_pointer < right_pointer and list_of_numbers[left_pointer] == list_of_numbers[left_pointer + 1]:
                        left_pointer += 1

                    while left_pointer < right_pointer and list_of_numbers[right_pointer] == list_of_numbers[right_pointer - 1]:
                        right_pointer -= 1

                    left_pointer += 1
                    right_pointer -= 1

                elif total_sum < 0:
                    left_pointer += 1

                else:
                    right_pointer -= 1

        return result_list