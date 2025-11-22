class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        for i, char in enumerate(s):
            shifted_value = (ord(char) - ord('a') + shifts[i]) % 26
            result.append(chr(shifted_value + ord('a')))
        return ''.join(result)