class Solution:
    def intToRoman(self, num: int) -> str:
        list_of_integer_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        list_of_roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numeral_string = ""
        index_variable = 0
        while num > 0:
            quotient_variable = num // list_of_integer_values[index_variable]
            for _ in range(quotient_variable):
                roman_numeral_string += list_of_roman_symbols[index_variable]
                num -= list_of_integer_values[index_variable]
            index_variable += 1
        return roman_numeral_string