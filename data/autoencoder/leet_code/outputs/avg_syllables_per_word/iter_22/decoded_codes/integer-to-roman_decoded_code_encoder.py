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
        roman_numeral = ""
        i = 0
        while num > 0:
            number_of_times = num // list_of_values[i]
            for _ in range(number_of_times):
                roman_numeral += list_of_symbols[i]
                num -= list_of_values[i]
            i += 1
        return roman_numeral