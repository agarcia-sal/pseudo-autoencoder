from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        for i in range(len(s)):
            base_value = ord(s[i]) - ord('a')
            shifted_value = base_value + shifts[i]
            wrapped_value = shifted_value % 26
            new_char = chr(wrapped_value + ord('a'))
            result.append(new_char)
        return ''.join(result)