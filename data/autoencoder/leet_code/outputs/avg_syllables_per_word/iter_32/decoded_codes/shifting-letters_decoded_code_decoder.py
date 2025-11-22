from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        # Update shifts array to represent cumulative shifts from right to left
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        for i in range(len(s)):
            # Calculate new character after applying shift modulo 26
            new_char_code = (ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a')
            result.append(chr(new_char_code))

        return ''.join(result)