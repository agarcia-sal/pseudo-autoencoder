class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_twenty = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]
        tens = [
            "Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return below_twenty[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_twenty[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        i = 0
        while num > 0:
            rem = num % 1000
            if rem != 0:
                result = helper(rem) + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()