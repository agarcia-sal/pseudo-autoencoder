class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        for i, ch in enumerate(s):
            numerical_value = ord(ch) - ord('a')
            shifted_value = numerical_value + shifts[i]
            wrapped_value = shifted_value % 26
            new_char = chr(ord('a') + wrapped_value)
            result.append(new_char)

        return ''.join(result)