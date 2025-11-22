class Solution:
    def appealSum(self, s: str) -> int:
        last_seen_positions = self.initialize_last_positions()
        total_appeal = 0
        current_appeal = 0
        for i in range(len(s)):
            current_character = s[i]
            character_index = self.map_char_to_index(current_character)
            difference = i - last_seen_positions[character_index]
            current_appeal += difference
            total_appeal += current_appeal
            last_seen_positions[character_index] = i
        return total_appeal

    def initialize_last_positions(self) -> list:
        return [-1] * 26

    def map_char_to_index(self, character: str) -> int:
        return ord(character) - ord('a')