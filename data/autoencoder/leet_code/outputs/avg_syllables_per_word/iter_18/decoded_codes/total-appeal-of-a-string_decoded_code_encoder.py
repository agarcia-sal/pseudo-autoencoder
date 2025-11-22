class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        total_appeal = 0
        current_appeal = 0

        for index, character in enumerate(s):
            character_index = ord(character) - ord('a')
            current_appeal += index - last[character_index]
            total_appeal += current_appeal
            last[character_index] = index

        return total_appeal