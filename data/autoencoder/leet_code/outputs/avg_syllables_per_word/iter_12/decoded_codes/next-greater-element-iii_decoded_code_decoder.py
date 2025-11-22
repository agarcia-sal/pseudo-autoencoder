class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        i = length - 2

        # Find first decreasing element from the right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1

        j = length - 1
        # Find element just larger than digits[i] from the right
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        prefix = digits[: i + 1]
        suffix = digits[i + 1 :]
        suffix.reverse()

        digits = prefix + suffix
        result = int(''.join(digits))
        if result > 2**31 - 1:
            return -1
        return result