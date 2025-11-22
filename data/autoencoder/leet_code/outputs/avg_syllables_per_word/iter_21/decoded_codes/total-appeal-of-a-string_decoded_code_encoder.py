class Solution:
    def appealSum(self, s: str) -> int:
        last = self.initialize_last_with_negative_one(26)
        total_appeal = 0
        current_appeal = 0

        for position_index, character in enumerate(s):
            index = self.convert_character_to_index(character)
            current_appeal += position_index - last[index]
            total_appeal += current_appeal
            last[index] = position_index

        return total_appeal

    def initialize_last_with_negative_one(self, count: int) -> list[int]:
        return [-1] * count

    def convert_character_to_index(self, character: str) -> int:
        return ord(character) - ord('a')