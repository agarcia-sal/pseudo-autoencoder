class Solution:
    def shiftingLetters(self, s, shifts):
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        for i in range(len(s)):
            shifted_value = (ord(s[i]) - ord('a') + shifts[i]) % 26
            result.append(chr(shifted_value + ord('a')))

        return ''.join(result)