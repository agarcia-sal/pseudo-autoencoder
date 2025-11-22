class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        # Find the length of the numbers where the nth digit is located
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Find the actual number that contains the nth digit
        start += (n - 1) // length

        digit_string = str(start)
        digit_position = (n - 1) % length
        result_character = digit_string[digit_position]

        return int(result_character)