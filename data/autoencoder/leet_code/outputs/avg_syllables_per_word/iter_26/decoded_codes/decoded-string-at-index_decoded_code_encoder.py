class Solution:
    def decodeAtIndex(self, input_string: str, target_index: int) -> str:
        decoded_length = 0

        # First pass: find the length of the decoded string
        for char in input_string:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1

        # Second pass: work backwards to find the character at target_index
        for char in reversed(input_string):
            target_index %= decoded_length

            if target_index == 0 and char.isalpha():
                return char

            if char.isdigit():
                decoded_length //= int(char)
            else:
                decoded_length -= 1