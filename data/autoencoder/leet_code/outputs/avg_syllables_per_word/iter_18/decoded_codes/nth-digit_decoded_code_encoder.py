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
        number_string = str(start)
        digit_position = (n - 1) % length
        result_digit = number_string[digit_position]

        return int(result_digit)