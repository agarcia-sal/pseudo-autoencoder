from typing import List

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_twenty: List[str] = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]
        tens: List[str] = [
            "Zero", "Ten", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands: List[str] = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            if n < 20:
                return below_twenty[n] + " "
            if n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            return below_twenty[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        i = 0
        while num > 0:
            remainder = num % 1000
            if remainder != 0:
                segment = helper(remainder) + thousands[i] + " "
                result = segment + result
            num //= 1000
            i += 1

        return result.strip()