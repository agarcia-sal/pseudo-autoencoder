class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        i = length - 2

        # Find first decreasing digit from the right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1

        # Find rightmost successor to the pivot
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Swap pivot and successor
        digits[i], digits[j] = digits[j], digits[i]

        # Reverse suffix
        digits[i + 1 :] = reversed(digits[i + 1 :])

        result = int("".join(digits))
        if result > 2**31 - 1:
            return -1
        return result