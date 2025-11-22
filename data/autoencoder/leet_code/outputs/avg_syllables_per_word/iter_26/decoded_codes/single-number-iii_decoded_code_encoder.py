class Solution:
    def singleNumber(self, list_of_numbers):
        xor_of_all_numbers = 0
        for number in list_of_numbers:
            xor_of_all_numbers ^= number

        differing_bit = xor_of_all_numbers & -xor_of_all_numbers

        first_unique_number = 0
        second_unique_number = 0

        for number in list_of_numbers:
            if number & differing_bit:
                first_unique_number ^= number
            else:
                second_unique_number ^= number

        return [first_unique_number, second_unique_number]