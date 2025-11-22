class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        result = []
        base_code = ord('a')
        for i in range(len(s)):
            character_code = ord(s[i])
            shifted_value = character_code - base_code + shifts[i]
            wrapped_value = shifted_value % 26
            new_character_code = wrapped_value + base_code
            new_character = chr(new_character_code)
            result.append(new_character)
        final_string = ''.join(result)
        return final_string