class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = self.convert_number_to_digit_list(num)
        last = self.create_last_occurrence_dictionary(digits)

        for i in range(len(digits)):
            d = int(digits[i])
            for d2 in range(9, d, -1):
                if d2 in last and last[d2] > i:
                    swapped_digits = self.swap_elements_in_list(digits, i, last[d2])
                    return self.convert_digit_list_to_number(swapped_digits)
        return num

    def convert_number_to_digit_list(self, number: int) -> list[str]:
        # Convert the number to a list of digit strings
        return list(str(number))

    def create_last_occurrence_dictionary(self, digit_list: list[str]) -> dict[int, int]:
        # Map each digit (as int) to its last index in digit_list
        last = {}
        for i, d in enumerate(digit_list):
            last[int(d)] = i
        return last

    def swap_elements_in_list(self, list_object: list[str], first_index: int, second_index: int) -> list[str]:
        # Swap elements at first_index and second_index in list_object
        list_object[first_index], list_object[second_index] = list_object[second_index], list_object[first_index]
        return list_object

    def convert_digit_list_to_number(self, digit_list: list[str]) -> int:
        # Join all elements into a string and convert to int
        return int(''.join(digit_list))