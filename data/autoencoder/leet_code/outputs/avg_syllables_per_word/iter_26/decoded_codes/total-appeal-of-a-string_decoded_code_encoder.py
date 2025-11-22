class Solution:
    def appealSum(self, s: str) -> int:
        last_seen_indices = [-1] * 26
        total_appeal_value = 0
        current_appeal_value = 0

        for i, char in enumerate(s):
            character_index = ord(char) - ord('a')
            current_appeal_value += i - last_seen_indices[character_index]
            total_appeal_value += current_appeal_value
            last_seen_indices[character_index] = i

        return total_appeal_value