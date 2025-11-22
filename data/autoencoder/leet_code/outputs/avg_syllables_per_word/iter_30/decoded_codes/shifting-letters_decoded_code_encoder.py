class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        for i in range(len(s)):
            char_pos = ord(s[i]) - ord('a')
            shifted_pos = (char_pos + shifts[i]) % 26
            new_char = chr(shifted_pos + ord('a'))
            result.append(new_char)
        return ''.join(result)