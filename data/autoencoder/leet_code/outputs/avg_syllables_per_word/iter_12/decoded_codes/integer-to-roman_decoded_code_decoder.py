class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_numeral = ""
        i = 0
        while num > 0:
            times = num // val[i]  # Calculate how many times val[i] fits into num
            for _ in range(times):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        return roman_numeral