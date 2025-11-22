class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        # Find the range in which the nth digit lies
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        start += (n - 1) // length
        digit_string = str(start)
        digit_index = (n - 1) % length
        return int(digit_string[digit_index])