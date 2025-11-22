class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        start += (n - 1) // length
        index = (n - 1) % length
        start_string = str(start)
        digit_char = start_string[index]
        digit = int(digit_char)
        return digit