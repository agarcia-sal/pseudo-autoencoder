class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        string_representation = str(abs(x))
        reversed_string = string_representation[::-1]
        reversed_x = int(reversed_string)
        result = sign * reversed_x
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result