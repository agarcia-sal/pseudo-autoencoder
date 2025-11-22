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
        digit_string = str(start)
        digit_index = (n - 1) % length
        digit_character = digit_string[digit_index]
        return int(digit_character)