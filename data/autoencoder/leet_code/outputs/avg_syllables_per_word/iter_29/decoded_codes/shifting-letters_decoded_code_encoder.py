class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        a_ord = ord('a')
        for i in range(len(s)):
            char_code_diff = ord(s[i]) - a_ord
            shifted_code = (char_code_diff + shifts[i]) % 26
            new_char_code = shifted_code + a_ord
            new_char = chr(new_char_code)
            result.append(new_char)
        return "".join(result)