class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        # First pass: find the length of the decoded string
        for char in s:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1

        # Second pass: decode from the end
        for char in reversed(s):
            k %= length
            if k == 0 and char.isalpha():
                return char
            if char.isdigit():
                length //= int(char)
            else:
                length -= 1