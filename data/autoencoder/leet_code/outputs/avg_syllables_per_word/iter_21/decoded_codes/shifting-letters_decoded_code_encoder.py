class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        base = ord('a')
        for i in range(len(s)):
            shifted_value = ord(s[i]) - base + shifts[i]
            wrapped_value = shifted_value % 26
            result.append(chr(wrapped_value + base))
        return ''.join(result)