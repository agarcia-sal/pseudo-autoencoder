class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = 0
        right = len(text) - 1
        left_part = ""
        right_part = ""
        k = 0

        while left < right:
            left_part += text[left]
            right_part = text[right] + right_part

            if left_part == right_part:
                k += 2
                left_part = ""
                right_part = ""

            left += 1
            right -= 1

        if left_part != "" or left == right:
            k += 1

        return k