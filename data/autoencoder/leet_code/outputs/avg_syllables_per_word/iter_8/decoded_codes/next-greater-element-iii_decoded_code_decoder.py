class Solution:
    def nextGreaterElement(self, n):
        digits = list(str(n))
        length = len(digits)

        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:
            return -1

        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        digits = digits[:i + 1] + digits[i + 1:][::-1]

        result = int("".join(digits))

        if result > (2**31) - 1:
            return -1

        return result