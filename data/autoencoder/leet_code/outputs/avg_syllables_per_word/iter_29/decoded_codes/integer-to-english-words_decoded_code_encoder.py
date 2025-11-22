class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_twenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return below_twenty[n] + " "
            elif n < 100:
                quotient, remainder = divmod(n, 10)
                return tens[quotient] + " " + helper(remainder)
            else:
                quotient, remainder = divmod(n, 100)
                return below_twenty[quotient] + " Hundred " + helper(remainder)

        result = ""
        i = 0

        while num > 0:
            remainder = num % 1000
            if remainder != 0:
                result = helper(remainder) + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()