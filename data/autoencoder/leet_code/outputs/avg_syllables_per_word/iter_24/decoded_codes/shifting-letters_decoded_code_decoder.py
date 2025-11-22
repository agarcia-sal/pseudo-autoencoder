class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        a_ord = ord('a')
        for i, ch in enumerate(s):
            original_val = ord(ch) - a_ord
            shifted_val = (original_val + shifts[i]) % 26
            result.append(chr(a_ord + shifted_val))
        return ''.join(result)