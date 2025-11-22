class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        for i in range(len(s)):
            original_character_value = ord(s[i]) - ord('a')
            shifted_value = original_character_value + shifts[i]
            wrapped_value = shifted_value % 26
            new_character_value = wrapped_value + ord('a')
            new_character = chr(new_character_value)
            result.append(new_character)
        return "".join(result)