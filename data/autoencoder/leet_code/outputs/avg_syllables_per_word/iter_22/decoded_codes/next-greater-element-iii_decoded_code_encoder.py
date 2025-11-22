class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        i = length - 2
        # Find the first digit that is smaller than the digit after it
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = length - 1
        # Find the digit just larger than digits[i]
        while digits[j] <= digits[i]:
            j -= 1
        # Swap
        digits[i], digits[j] = digits[j], digits[i]
        # Reverse the suffix starting at i+1
        digits[i + 1 :] = reversed(digits[i + 1 :])
        result = int(''.join(digits))
        if result > (2 ** 31) - 1:
            return -1
        return result