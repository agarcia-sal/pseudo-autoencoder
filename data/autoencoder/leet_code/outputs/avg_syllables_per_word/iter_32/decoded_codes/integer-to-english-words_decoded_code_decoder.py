from typing import List

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "zero"

        below_twenty: List[str] = [
            "",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]

        tens: List[str] = [
            "",
            "",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]

        thousands: List[str] = [
            "",
            "thousand",
            "million",
            "billion"
        ]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return below_twenty[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:  # n < 1000 guaranteed here
                return below_twenty[n // 100] + " hundred " + helper(n % 100)

        result = ""
        i = 0

        while num > 0:
            curr = num % 1000
            if curr != 0:
                part = helper(curr) + thousands[i]
                if part != "":
                    part += " "
                result = part + result
            num //= 1000
            i += 1

        return result.strip()