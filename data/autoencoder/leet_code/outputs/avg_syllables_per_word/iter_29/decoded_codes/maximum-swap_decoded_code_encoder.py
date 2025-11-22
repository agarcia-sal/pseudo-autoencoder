class Solution:
    def maximumSwap(self, num: int) -> int:
        digits_list = list(str(num))
        last_occurrence_dictionary = {}

        for index, digit_character in enumerate(digits_list):
            digit_number = int(digit_character)
            last_occurrence_dictionary[digit_number] = index

        for index, digit_character in enumerate(digits_list):
            digit_number = int(digit_character)
            for candidate_digit in range(9, digit_number, -1):
                if last_occurrence_dictionary.get(candidate_digit, -1) > index:
                    swap_index = last_occurrence_dictionary[candidate_digit]
                    digits_list[index], digits_list[swap_index] = digits_list[swap_index], digits_list[index]
                    return int("".join(digits_list))

        return num