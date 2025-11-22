class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        absolute_x = abs(x)
        reversed_string_x = str(absolute_x)[::-1]
        reversed_x = int(reversed_string_x)
        result = sign * reversed_x
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result