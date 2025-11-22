class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits_list = self.convert_number_to_list_of_digits(n)
        length_of_digits = len(digits_list)

        i_index = length_of_digits - 2
        while i_index >= 0 and digits_list[i_index] >= digits_list[i_index + 1]:
            i_index -= 1

        if i_index == -1:
            return -1

        j_index = length_of_digits - 1
        while digits_list[j_index] <= digits_list[i_index]:
            j_index -= 1

        self.swap_elements(digits_list, i_index, j_index)
        self.reverse_sublist(digits_list, i_index + 1, length_of_digits - 1)

        result_integer = self.convert_list_of_digits_to_number(digits_list)

        if result_integer > 2**31 - 1:
            return -1

        return result_integer

    def convert_number_to_list_of_digits(self, n: int) -> list[int]:
        return [int(d) for d in str(n)]

    def swap_elements(self, list_collection: list[int], index_one: int, index_two: int) -> None:
        list_collection[index_one], list_collection[index_two] = list_collection[index_two], list_collection[index_one]

    def reverse_sublist(self, list_collection: list[int], start_index: int, end_index: int) -> None:
        while start_index < end_index:
            self.swap_elements(list_collection, start_index, end_index)
            start_index += 1
            end_index -= 1

    def convert_list_of_digits_to_number(self, digits_list: list[int]) -> int:
        result = 0
        for digit in digits_list:
            result = result * 10 + digit
        return result