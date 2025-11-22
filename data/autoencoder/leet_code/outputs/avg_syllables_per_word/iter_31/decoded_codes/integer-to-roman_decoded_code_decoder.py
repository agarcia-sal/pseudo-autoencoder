class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_numeral = []
        index = 0
        while num > 0:
            count = num // values[index]
            for _ in range(count):
                roman_numeral.append(symbols[index])
                num -= values[index]
            index += 1
        return "".join(roman_numeral)