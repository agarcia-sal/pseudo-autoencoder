class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = self.ConvertNumberToDigitList(n)
        length = len(digits)
        marker = length

        for i in range(length - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = self.ConvertDigitToString(int(digits[i - 1]) - 1)
                marker = i

        for i in range(marker, length):
            digits[i] = '9'

        return self.ConvertDigitListToInteger(digits)

    def ConvertNumberToDigitList(self, number: int) -> list:
        # Converts an integer to list of string digits
        return list(str(number))

    def ConvertDigitToString(self, digit: int) -> str:
        # Converts a single integer digit (0-9) to a string digit
        return str(digit)

    def ConvertDigitListToInteger(self, digit_list: list) -> int:
        # Converts a list of string digits to an integer
        return int(''.join(digit_list))