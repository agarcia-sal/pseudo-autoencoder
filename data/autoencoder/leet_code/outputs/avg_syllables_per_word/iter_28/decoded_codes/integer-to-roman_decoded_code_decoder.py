from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        val: List[int] = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms: List[str] = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        roman_numeral = []
        i = 0
        while num > 0:
            count = num // val[i]
            roman_numeral.append(syms[i] * count)
            num -= val[i] * count
            i += 1
        return "".join(roman_numeral)