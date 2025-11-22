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
        string_representation = str(start)
        digit_position = (n - 1) % length

        return int(string_representation[digit_position])