class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_x = AbstractReverseDigits(abs(x))
        result = sign * reversed_x
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result


def AbstractReverseDigits(positive_integer: int) -> int:
    reversed_num = 0
    while positive_integer > 0:
        reversed_num = reversed_num * 10 + positive_integer % 10
        positive_integer //= 10
    return reversed_num