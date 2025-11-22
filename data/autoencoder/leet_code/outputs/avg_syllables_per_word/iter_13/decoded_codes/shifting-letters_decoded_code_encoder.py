class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total_shifts = 0
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts

        result = []
        a_ord = ord('a')
        for i, ch in enumerate(s):
            alphabetical_position = ord(ch) - a_ord + shifts[i]
            wrapped_position = alphabetical_position % 26
            new_character = chr(a_ord + wrapped_position)
            result.append(new_character)

        return ''.join(result)