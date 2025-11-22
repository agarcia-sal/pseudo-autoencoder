class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        absolute_x = abs(x)
        string_representation = str(absolute_x)
        reversed_string = string_representation[::-1]
        reversed_x = int(reversed_string)
        result = sign * reversed_x
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result