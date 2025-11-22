class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = [
            chr((ord(c) - ord('a') + shifts[i]) % 26 + ord('a'))
            for i, c in enumerate(s)
        ]
        return ''.join(result)