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
        digit_position = (n - 1) % length
        start_string = str(start)
        desired_digit_character = start_string[digit_position]
        desired_digit = int(desired_digit_character)
        return desired_digit