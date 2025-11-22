class Solution:
    def intToRoman(self, num: int) -> str:
        list_of_values = [
            1000, 900, 500, 400,
            100, 90, 50, 40, 
            10, 9, 5, 4, 1
        ]
        list_of_symbols = [
            "M", "CM", "D", "CD", 
            "C", "XC", "L", "XL", 
            "X", "IX", "V", "IV", "I"
        ]

        roman_numeral_string = ""
        index_i = 0
        while num > 0:
            how_many_times = num // list_of_values[index_i]
            for _ in range(how_many_times):
                roman_numeral_string += list_of_symbols[index_i]
                num -= list_of_values[index_i]
            index_i += 1
        return roman_numeral_string