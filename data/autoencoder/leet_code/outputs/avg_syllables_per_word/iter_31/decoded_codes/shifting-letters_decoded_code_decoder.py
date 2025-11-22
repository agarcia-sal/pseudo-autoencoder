from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        # Compute the cumulative shifts in reverse order
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        for i, ch in enumerate(s):
            new_character_index = (ord(ch) - ord('a') + shifts[i]) % 26
            new_character = chr(new_character_index + ord('a'))
            result.append(new_character)

        return ''.join(result)