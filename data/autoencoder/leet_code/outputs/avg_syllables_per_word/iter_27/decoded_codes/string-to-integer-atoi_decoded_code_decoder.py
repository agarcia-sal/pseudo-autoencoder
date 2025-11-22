class Solution:
    def myAtoi(self, s: str) -> int:
        maximum_32_bit_signed_integer = 2**31 - 1
        minimum_32_bit_signed_integer = -2**31
        result = 0
        index = 0
        length_of_string = len(s)
        sign = 1

        while index < length_of_string and s[index].isspace():
            index += 1

        if index < length_of_string and (s[index] == '+' or s[index] == '-'):
            if s[index] == '-':
                sign = -1
            else:
                sign = 1
            index += 1

        while index < length_of_string and s[index].isdigit():
            digit = int(s[index])
            if result > (maximum_32_bit_signed_integer - digit) // 10:
                return maximum_32_bit_signed_integer if sign == 1 else minimum_32_bit_signed_integer
            result = result * 10 + digit
            index += 1

        return sign * result