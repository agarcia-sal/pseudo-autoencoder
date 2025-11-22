class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for index in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[index]
            shifts[index] = total_shifts
        result = []
        for index in range(len(s)):
            original_character_position = ord(s[index]) - ord('a')
            shifted_character_position = (original_character_position + shifts[index]) % 26
            new_character_code = shifted_character_position + ord('a')
            result.append(chr(new_character_code))
        return ''.join(result)