class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        n = len(shifts)
        for i in range(n - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        for i, ch in enumerate(s):
            shift_value = shifts[i]
            original_char_position = ord(ch) - ord('a')
            new_char_position = (original_char_position + shift_value) % 26
            new_character = chr(new_char_position + ord('a'))
            result.append(new_character)

        return "".join(result)