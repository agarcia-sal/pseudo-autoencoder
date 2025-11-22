class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = 0
        index = 0
        n = len(s)
        sign = 1

        # Skip leading spaces
        while index < n and s[index] == ' ':
            index += 1

        # Check sign
        if index < n and (s[index] == '+' or s[index] == '-'):
            if s[index] == '-':
                sign = -1
            index += 1

        # Parse digits and handle overflow
        while index < n and s[index].isdigit():
            digit = int(s[index])
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1

        return sign * result