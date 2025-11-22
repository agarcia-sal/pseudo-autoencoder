class Solution:
    def intToRoman(self, num: int) -> str:
        val = self.get_roman_values()
        syms = self.get_roman_symbols()
        roman_numeral = ""
        i = 0
        while num > 0:
            count = num // val[i]
            for _ in range(count):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        return roman_numeral

    def get_roman_values(self):
        return [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def get_roman_symbols(self):
        return ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]