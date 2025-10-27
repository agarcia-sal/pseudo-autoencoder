class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs_str = str(abs(x))
        reversed_str = x_abs_str[::-1]
        reversed_num = int(reversed_str)
        result = sign * reversed_num
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result