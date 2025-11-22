class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        marker = length
        for index in range(length - 1, 0, -1):
            if digits[index] < digits[index - 1]:
                digits[index - 1] = str(int(digits[index - 1]) - 1)
                marker = index
        for index in range(marker, length):
            digits[index] = '9'
        return int("".join(digits))