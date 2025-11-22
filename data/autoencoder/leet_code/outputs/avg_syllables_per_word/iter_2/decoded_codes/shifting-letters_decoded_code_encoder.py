class Solution:
    def shiftingLetters(self, s, shifts):
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        for i in range(len(s)):
            new_char_code = (ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a')
            new_char = chr(new_char_code)
            result.append(new_char)
        return ''.join(result)