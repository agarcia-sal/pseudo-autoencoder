class Solution:
    def shiftingLetters(self, s, shifts):
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        a_ord = ord('a')
        for i in range(len(s)):
            numeric_value = ord(s[i]) - a_ord
            shifted_value = numeric_value + shifts[i]
            wrapped_value = shifted_value % 26
            new_character = chr(wrapped_value + a_ord)
            result.append(new_character)
        return ''.join(result)