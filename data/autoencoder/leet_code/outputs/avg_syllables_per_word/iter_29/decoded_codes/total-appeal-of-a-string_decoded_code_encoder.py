class Solution:
    def appealSum(self, s: str) -> int:
        last_seen_indices = [-1] * 26
        total_appeal = 0
        current_appeal = 0
        position = 0

        for character in s:
            character_index = ord(character) - ord('a')
            difference = position - last_seen_indices[character_index]
            current_appeal += difference
            total_appeal += current_appeal
            last_seen_indices[character_index] = position
            position += 1

        return total_appeal