class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        a_ord = ord('a')
        for i, ch in enumerate(s):
            numeric_value = ord(ch) - a_ord
            shifted_value = (numeric_value + shifts[i]) % 26
            new_character = chr(shifted_value + a_ord)
            result.append(new_character)
        return ''.join(result)