from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        for i in range(len(s)):
            character_position = ord(s[i]) - ord('a')
            shifted_position = character_position + shifts[i]
            wrapped_position = shifted_position % 26
            new_character = chr(wrapped_position + ord('a'))
            result.append(new_character)

        return ''.join(result)