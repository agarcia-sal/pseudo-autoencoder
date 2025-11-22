class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numeral = []
        for i in range(len(val)):
            count = num // val[i]
            roman_numeral.append(syms[i] * count)
            num -= val[i] * count
            if num == 0:
                break
        return "".join(roman_numeral)